"""Core functions for the Finger Slash game."""

import json
from datetime import date

import numpy as np


def track_fingertip(x: float, y: float, width: int, height: int) -> tuple[int, int]:
    """Convert normalized fingertip coordinates to screen coordinates.

    Args:
        x (float): Normalized horizontal coordinate (0 to 1).
        y (float): Normalized vertical coordinate (0 to 1).
        width (int): Game screen width in pixels.
        height (int): Game screen height in pixels.

    Returns:
        tuple[int, int]: Fingertip position in screen pixels.

    Raises:
        ValueError: If coordinates or dimensions are invalid.

    Examples:
        >>> track_fingertip(0.5, 0.5, 1280, 720)
        (640, 360)
    """
    if not (0.0 <= x <= 1.0 and 0.0 <= y <= 1.0):
        raise ValueError("x and y must be between 0 and 1")
    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive")

    # 버림 후 마지막 픽셀(width - 1)로 제한해 x=1.0이 화면 밖으로 나가지 않게 함
    px = min(int(x * width), width - 1)
    py = min(int(y * height), height - 1)
    return (px, py)


def detect_slice(
    previous: tuple[float, float],
    current: tuple[float, float],
    center: tuple[float, float],
    radius: float,
    min_speed: float,
) -> bool:
    """Determine whether a fingertip movement slices an object.

    Args:
        previous (tuple[float, float]): Previous fingertip position.
        current (tuple[float, float]): Current fingertip position.
        center (tuple[float, float]): Center of the fruit or bomb.
        radius (float): Object collision radius.
        min_speed (float): Minimum fingertip movement per frame.

    Returns:
        bool: True if the movement intersects the object fast enough.

    Raises:
        ValueError: If radius or minimum speed is invalid.
        NotImplementedError: Until the function is implemented.

    Examples:
        >>> detect_slice((0, 50), (100, 50), (50, 50), 20, 10)
        True
    """
    if not np.isfinite(radius) or radius <= 0:
        raise ValueError("radius must be a positive finite number")
    if not np.isfinite(min_speed) or min_speed < 0:
        raise ValueError("min_speed must be a non-negative finite number")

    start = np.asarray(previous, dtype=float)
    end = np.asarray(current, dtype=float)
    point = np.asarray(center, dtype=float)

    segment = end - start
    length_sq = float(np.dot(segment, segment))
    if np.sqrt(length_sq) < min_speed:
        return False

    # 손이 멈춘 경우(길이 0)는 0으로 나누지 않고 시작점과의 거리로 판정
    if length_sq == 0.0:
        t = 0.0
    else:
        t = float(np.clip(np.dot(point - start, segment) / length_sq, 0.0, 1.0))
    closest = start + t * segment
    return bool(np.linalg.norm(point - closest) < radius)


def save_high_score(score: int, path: str = "highscore.json") -> bool:
    """Save a new high score if it exceeds the previous record.

    Args:
        score (int): Current game score.
        path (str): Path to the high-score JSON file.

    Returns:
        bool: True if a new high score was saved, otherwise False.

    Raises:
        ValueError: If the score is negative.
        OSError: If the file cannot be written.
        NotImplementedError: Until the function is implemented.

    Examples:
        >>> save_high_score(100)
        True
    """
    if score < 0:
        raise ValueError("score must not be negative")

    best = _load_best_score(path)
    if best is not None and score <= best:
        return False

    with open(path, "w", encoding="utf-8") as f:
        json.dump({"score": score, "date": date.today().isoformat()}, f)
    return True


def _load_best_score(path: str) -> "int | None":
    # 파일이 없거나 깨졌으면 기록 없음(None)으로 보고 새 점수로 덮어쓰게 함
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError, UnicodeDecodeError):
        return None
    if isinstance(data, dict) and type(data.get("score")) is int:
        return data["score"]
    return None
