import base64
import json
import os
from pathlib import Path
from typing import Annotated, Any, Tuple, Union

import cv2
import numpy as np
from loguru import logger
from pydantic import BeforeValidator, PlainSerializer
from rich import print

from phosphobot.types import VideoCodecs


class NumpyEncoder(json.JSONEncoder):
    """Custom encoder for numpy data types"""

    def default(self, obj):
        logger.info(f"Encoding with NumpyEncoder object type({type(obj)}) {obj}")
        if isinstance(obj, np.ndarray):
            logger.debug(f"Encoding NumpyEncoder numpy array of shape {obj.shape}")
            return {
                "_type": "ndarray",
                "data": obj.tolist(),
                "dtype": str(obj.dtype),
                "shape": obj.shape,
            }
        return json.JSONEncoder.default(self, obj)


def decode_numpy(dct: dict) -> Union[np.ndarray, dict]:
    """Custom decoder. Reads the encoded numpy array from the JSON file."""
    if isinstance(dct, dict) and dct.get("_type") == "ndarray":
        return np.array(dct["data"], dtype=np.dtype(dct["dtype"]))
    if "__numpy__" in dct:
        data = base64.b64decode(dct["__numpy__"])
        arr = np.frombuffer(data, dtype=np.dtype(dct["dtype"]))
        arr = arr.reshape(dct["shape"])
        return arr
    return dct


def nd_array_custom_before_validator(x: Any) -> np.ndarray:
    # custom before validation logic
    if isinstance(x, list):
        return np.array(x)
    elif isinstance(x, np.ndarray):
        return x
    else:
        raise ValueError("Invalid type for numpy array")


def nd_array_custom_serializer(x: np.ndarray):
    # custom serialization logic: convert to list
    return x.tolist()


# Custom type for numpy array. Stores np.ndarray as list in JSON.
NdArrayAsList = Annotated[
    np.ndarray,
    BeforeValidator(nd_array_custom_before_validator),
    PlainSerializer(nd_array_custom_serializer, return_type=list),
]


def create_video_file(
    frames: np.ndarray,
    target_size: Tuple[int, int],
    output_path: str,
    fps: float,
    codec: VideoCodecs,
) -> str | Tuple[str, str]:
    """
    Create a video file from a list of frames and resize video to target size.
    For stereo cameras (aspect ratio >= 8/3), creates separate left and right video files.

    Args:
        frames (list of np.ndarray): List of frames in RGB format.
        target_size (Tuple[int, int]): Target dimensions (width, height) for the output video.
        output_path (str): Path to save the video file.
        fps (float): Frames per second for the video.
        codec (str): FourCC codec for the video. Defaults to "mp4v" (MPEG-4 for MP4).

    Returns:
        Union[str, Tuple[str, str]]: Path(s) to created video file(s). Returns tuple of paths for stereo.

    Raises:
        ValueError: If frames are empty or incorrectly formatted.
        RuntimeError: If the video writer cannot be initialized.
    """
    # Check if stereo camera based on aspect ratio
    sample_frame = frames[0]
    aspect_ratio = sample_frame.shape[1] / sample_frame.shape[0]  # width/height
    is_stereo = aspect_ratio >= 8 / 3

    logger.info(
        f"Creating video file - stereo: {is_stereo} - Aspect ratio: {aspect_ratio}"
    )

    logger.info(f"Target size: {target_size}")

    def init_video_writer(path: str, size: Tuple[int, int]) -> cv2.VideoWriter:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(path), exist_ok=True)
        logger.info(f"Creating video file at path: {path}")

        fourcc = cv2.VideoWriter_fourcc(*codec)  # type: ignore
        out = cv2.VideoWriter(path, fourcc, fps, size)

        if not out.isOpened():
            try:
                out.open(path, fourcc, fps, size)
            except Exception as e:
                logger.error(f"Error while creating video file: {e}")
                raise RuntimeError(f"Error while creating video: {e}")
        return out

    def process_frame(frame: np.ndarray, target_size: Tuple[int, int]) -> np.ndarray:
        if frame.dtype != np.uint8:
            frame = np.clip(frame, 0, 255).astype(np.uint8)
        resized_frame = cv2.resize(frame, target_size, interpolation=cv2.INTER_AREA)
        return cv2.cvtColor(resized_frame, cv2.COLOR_RGB2BGR)

    if is_stereo:
        # Split path for stereo output
        path = output_path.split("/episode")
        left_path = f"{path[0]}.left/episode{path[1]}"
        right_path = f"{path[0]}.right/episode{path[1]}"

        logger.info(
            f"Splitting stereo video into left and right - paths: {left_path}, {right_path}"
        )

        # Initialize writers for both streams
        out_left = init_video_writer(left_path, target_size)
        out_right = init_video_writer(right_path, target_size)

        frame_width = sample_frame.shape[1] // 2  # Split width in half for stereo

        for frame in frames:
            # Split frame into left and right
            left_frame = frame[:, :frame_width]
            right_frame = frame[:, frame_width:]

            # Process and write each frame
            out_left.write(process_frame(left_frame, target_size))
            out_right.write(process_frame(right_frame, target_size))

        out_left.release()
        out_right.release()

        print(f"""[green]Left output path: {left_path}
Right output path: {right_path}
fps: {fps}
codec: {codec}
target_size of each video: {target_size}[/green]""")
        return left_path, right_path

    else:
        # Single camera processing
        out = init_video_writer(output_path, target_size)

        for frame in frames:
            out.write(process_frame(frame, target_size))

        out.release()

        print(f"""[green]Output path: {output_path}
Fps: {fps}
codec: {codec}
Target_size of video: {target_size}[/green]""")
        return output_path


def get_home_app_path() -> Path:
    """
    Return the path to the app's folder in the user's home directory.
    This is used to store user-specific data.

    It's platform dependent.

    user_home/
        phosphobot/
            calibration/
            recordings/
            ...
    """
    home_path = Path.home() / "phosphobot"
    # Create the folder if it doesn't exist
    home_path.mkdir(parents=True, exist_ok=True)
    # Create subfolders
    (home_path / "calibration").mkdir(parents=True, exist_ok=True)
    (home_path / "recordings").mkdir(parents=True, exist_ok=True)
    return home_path
