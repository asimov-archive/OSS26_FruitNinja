"""Core functions for the Finger Slash game."""


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
        NotImplementedError: Until the function is implemented.

    Examples:
        >>> track_fingertip(0.5, 0.5, 1280, 720)
        (640, 360)
    """
    raise NotImplementedError


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
    raise NotImplementedError


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
    raise NotImplementedError
