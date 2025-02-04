import logging
from enum import Enum
from pathlib import Path
from typing import Literal

from dask.array.core import Array
import dask.array as da
import xarray as xr
import numpy as np
import torch
import rioxarray
from huggingface_hub import hf_hub_download
from numpy import ndarray

from segmentmytif.logging_config import log_duration, log_array
from segmentmytif.utils.io import save_tiff, read_geotiff
from segmentmytif.utils.models import UNet

NUM_FLAIR_CLASSES = 19
DEFAULT_CHUNK_OVERLAP = 25  # Default chunk overlap size for feature extraction
logger = logging.getLogger(__name__)


class FeatureType(Enum):
    IDENTITY = 1
    FLAIR = 2

    @staticmethod
    def from_string(s):
        try:
            return FeatureType[s]
        except KeyError:
            raise ValueError()


def get_features(
    raster: xr.DataArray,
    raster_path: Path,
    feature_type: FeatureType,
    features_path: Path,
    chunk_overlap: int = DEFAULT_CHUNK_OVERLAP,
    compute_mode: Literal["normal", "parallel", "safe"] = "normal",
    **extractor_kwargs,
):
    """Extract features from the input data, or load them from disk if they have already been extracted.

    :param raster: raster data as xr.DataArray, read by rioxarray
    :param raster_path: path to the raster tiff file
    :param feature_type: See FeatureType enum for options.
    :param features_path: Path used for caching features
    :param chunk_overlap: Overlap between chunks when chunk-wise processing is enanbled
    :param extractor_kwargs: options for the feature extractor
    :return: extracted features as xr.DataArray
    """
    if feature_type == FeatureType.IDENTITY:
        return raster

    if features_path is None:
        features_path = get_features_path(raster_path, feature_type)
    if not features_path.exists():
        extract_and_save_features(raster, feature_type, chunk_overlap, features_path, extractor_kwargs)

    match compute_mode:
        case "normal":
            loaded_features = rioxarray.open_rasterio(features_path)
        case "parallel" | "safe":
            # Unpack the chunk sizes from the input raster
            chunks = {
                "band": raster.chunksizes["band"][0],
                "x": raster.chunksizes["x"][0],
                "y": raster.chunksizes["y"][0],
            }
            loaded_features = rioxarray.open_rasterio(features_path, chunks=chunks)
    msg = f"Loading {feature_type.name} features (shape {loaded_features.shape}) from {features_path}"
    logger.info(msg)

    return loaded_features


def extract_and_save_features(raster, feature_type, chunk_overlap, features_path, extractor_kwargs):
    msg = (
        f"No existing {feature_type.name} features found at {features_path} "
        f"for input data with shape {raster.data.shape}"
    )
    logger.info(msg)
    with log_duration(f"Extracting {feature_type.name} features", logger):
        features_data = extract_features(raster.data, feature_type, chunk_overlap, **extractor_kwargs)
    log_array(features_data, logger, array_name=f"{feature_type.name} features")
    # Create xarray DataArray with the extracted features
    # Keep the geospatial information from the input raster
    features = raster.isel(band=0).drop_vars(["band"]).expand_dims(band=features_data.shape[0])
    features.data = features_data
    # Save the features to disk
    msg = f"Saving {feature_type.name} features (shape {features_data.shape}) to {features_path}"
    logger.info(msg)
    features.rio.to_raster(features_path)


def extract_features(input_data, feature_type, chunk_overlap=16, **extractor_kwargs):
    extractor = {
        FeatureType.FLAIR: extract_flair_features,
    }[feature_type]

    # If dask array, map feature extraction function to each block
    # The blockwise extraction is only applied to FLAIR features
    # FeatureType.IDENTITY directly returns the input data, thus no need to map_overlap
    if isinstance(input_data, Array):
        # Make template dask array according to the extractor
        if feature_type == FeatureType.FLAIR:
            # If FLAIR, output features has bands * NUM_FLAIR_CLASSES
            meta = da.zeros_like(
                input_data,
                shape=(input_data.shape[0] * NUM_FLAIR_CLASSES, input_data.shape[1], input_data.shape[2]),
            )
        else:
            msg = f"Unsupported feature type: {feature_type}"
            raise ValueError(msg)

        # Feature extraction per block with overlap
        features = input_data.map_overlap(
            extractor,
            **extractor_kwargs,
            depth=(0, chunk_overlap, chunk_overlap),
            boundary="none",
            meta=meta,
        )

        # Since extractor changed the shape of the data
        # We call "compute_chunk_sizes" to align the shape with meta
        features = features.compute_chunk_sizes()

    else:
        features = extractor(input_data, **extractor_kwargs)

    return features


def extract_identity_features(input_data: ndarray) -> ndarray:
    return input_data


def extract_flair_features(input_data: ndarray, model_scale=1.0) -> ndarray:
    """

    :param input_data: Array-like input data as stored in TIFs. Shape: [n_bands, height, width]
    :param model_scale: Scale of the model to use. Must be one of [1.0, 0.5, 0.25, 0.125]
    :return: Features extracted from the input data
    """
    logger.info(f"Using UNet at scale {model_scale}")
    model, device = load_model(model_scale)
    n_bands = input_data.shape[0]

    outputs = []
    for i_band in range(n_bands):
        input_band = torch.from_numpy(input_data[None, i_band : i_band + 1, :, :]).float().to(device)
        padded_input = pad(input_band, band_name=i_band)
        padded_current_predictions = model(padded_input).detach().numpy()
        current_predictions = padded_current_predictions[:, :, : input_band.shape[2], : input_band.shape[3]]  # unpad
        outputs.append(current_predictions)
    output = np.concatenate(outputs, axis=1)
    return output[0, :, :, :]



def load_model(model_scale:float, models_dir: Path = Path("models")):
    """
    Load the model from disk and return it along with the device it's loaded on to.
    :param model_scale: Scale of the model to use. Must be one of [1.0, 0.5, 0.25, 0.125]
    :param models_dir: Path to the directory containing the model files
    :return: Torch model and the device it's loaded on to
    """
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = UNet(in_channels=1, num_classes=NUM_FLAIR_CLASSES, model_scale=model_scale)
    file_name = get_flair_model_file_name(model_scale)
    model_path = models_dir / file_name

    if not model_path.exists():
        logger.info(f"Model not found at '{model_path}', downloading from Hugging Face")
        hf_hub_download(repo_id="DroneML/FLAIR-feature-extractor", filename=file_name, local_dir=models_dir)

    state = torch.load(model_path, map_location=device, weights_only=True)

    model.load_state_dict(state)
    model.eval()
    return model, device


def pad(input_band, band_name):
    """
    Pad the input band, single-sided at the end of width and height axis, to make its dimensions divisible by 16.
    :param input_band: Input band to pad
    :return: Padded input
    """
    width = input_band.shape[2]
    height = input_band.shape[3]
    if width % 16 == 0 and height % 16 == 0:
        padded = input_band
    else:
        pad_width = 16 - width % 16
        pad_height = 16 - height % 16
        padded = torch.nn.functional.pad(input_band, (0, pad_height, 0, pad_width))
        logger.info(
            f"Added temporary padding for band {band_name}: (original {height} x {width})"
            f" -> (padded {height + pad_height} x {width + pad_width})"
        )

    return padded


def get_flair_model_file_name(model_scale: float) -> str:
    scale_mapping = {1.0: "1_0", 0.5: "0_5", 0.25: "0_25", 0.125: "0_125"}

    scale = None
    for k, v in scale_mapping.items():
        if np.isclose(model_scale, k, atol=0, rtol=0.1):
            scale = v
            break
    if scale is None:
        raise ValueError(f"Unsupported model scale selected ({model_scale}), choose from {scale_mapping.keys()}")

    return f"flair_toy_ep10_scale{scale}.pth"


def get_features_path(raster_path: Path, features_type: FeatureType) -> Path:
    if features_type == FeatureType.IDENTITY:
        return raster_path
    return raster_path.parent / f"{raster_path.stem}_{features_type.name}{raster_path.suffix}"
