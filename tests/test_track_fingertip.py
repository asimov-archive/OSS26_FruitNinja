"""track_fingertip 함수 테스트."""

import math

import pytest

from fruit_ninja import track_fingertip

WIDTH, HEIGHT = 1280, 720


def test_center():
    assert track_fingertip(0.5, 0.5, WIDTH, HEIGHT) == (640, 360)


def test_top_left():
    assert track_fingertip(0.0, 0.0, WIDTH, HEIGHT) == (0, 0)


def test_bottom_right_stays_on_screen():
    assert track_fingertip(1.0, 1.0, WIDTH, HEIGHT) == (WIDTH - 1, HEIGHT - 1)


def test_returns_tuple_of_two_ints():
    result = track_fingertip(0.3, 0.7, WIDTH, HEIGHT)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(type(v) is int for v in result)


@pytest.mark.parametrize(
    ("x", "y"),
    [(-0.1, 0.5), (1.1, 0.5), (0.5, -0.1), (0.5, 1.1)],
)
def test_out_of_range_coordinates_raise(x, y):
    with pytest.raises(ValueError):
        track_fingertip(x, y, WIDTH, HEIGHT)


@pytest.mark.parametrize(
    ("width", "height"),
    [(0, HEIGHT), (-1, HEIGHT), (WIDTH, 0), (WIDTH, -1)],
)
def test_non_positive_dimensions_raise(width, height):
    with pytest.raises(ValueError):
        track_fingertip(0.5, 0.5, width, height)


@pytest.mark.parametrize(("x", "y"), [(math.nan, 0.5), (0.5, math.nan)])
def test_nan_coordinates_raise(x, y):
    with pytest.raises(ValueError):
        track_fingertip(x, y, WIDTH, HEIGHT)
