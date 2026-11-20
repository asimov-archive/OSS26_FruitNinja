"""detect_slice 함수 테스트."""

import math

import pytest

from fruit_ninja import detect_slice


def test_hit():
    assert detect_slice((0, 50), (100, 50), (50, 50), 20, 10) is True


def test_miss():
    assert detect_slice((0, 50), (100, 50), (50, 100), 20, 10) is False


def test_too_slow():
    assert detect_slice((0, 50), (5, 50), (3, 50), 20, 10) is False


def test_movement_exactly_min_speed_counts():
    # 이동 거리 10 == min_speed 10 이면 속도 조건을 통과한다.
    assert detect_slice((0, 50), (10, 50), (5, 50), 20, 10) is True


def test_segment_stops_short_of_fruit():
    # 무한 직선이라면 맞지만, 선분 끝(20, 50)에서 중심까지 거리가 30 > 20 이다.
    assert detect_slice((0, 50), (20, 50), (50, 50), 20, 10) is False


def test_tangent_is_not_a_hit():
    # 가장 가까운 거리 == 반지름 이면 strict < 비교라서 False.
    assert detect_slice((0.0, 0.0), (100.0, 0.0), (50.0, 20.0), 20.0, 10) is False


def test_diagonal_hit():
    assert detect_slice((0, 0), (100, 100), (50, 50), 5, 10) is True


def test_stationary_inside_fruit_with_zero_min_speed():
    assert detect_slice((50, 50), (50, 50), (55, 50), 20, 0) is True


def test_stationary_with_positive_min_speed():
    assert detect_slice((50, 50), (50, 50), (55, 50), 20, 1) is False


def test_accepts_lists_and_ints():
    assert detect_slice([0, 50], [100, 50], [50, 50], 20, 10) is True
    assert detect_slice((0.0, 50.0), (100.0, 50.0), (50.0, 50.0), 20.0, 10.0) is True


def test_returns_builtin_bool():
    assert type(detect_slice((0, 50), (100, 50), (50, 50), 20, 10)) is bool
    assert type(detect_slice((0, 50), (100, 50), (50, 100), 20, 10)) is bool


@pytest.mark.parametrize("radius", [0, -1, math.nan, math.inf])
def test_invalid_radius_raises(radius):
    with pytest.raises(ValueError):
        detect_slice((0, 50), (100, 50), (50, 50), radius, 10)


@pytest.mark.parametrize("min_speed", [-1, math.nan, math.inf])
def test_invalid_min_speed_raises(min_speed):
    with pytest.raises(ValueError):
        detect_slice((0, 50), (100, 50), (50, 50), 20, min_speed)


def test_zero_min_speed_is_allowed():
    assert detect_slice((0, 50), (100, 50), (50, 50), 20, 0) is True
