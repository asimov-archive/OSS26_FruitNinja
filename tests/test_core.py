"""fruit_ninja.core 공개 함수 테스트."""

import json
import math
from datetime import date

import pytest

from fruit_ninja import detect_slice, save_high_score, track_fingertip

WIDTH, HEIGHT = 1280, 720


# ---------------------------------------------------------------------------
# track_fingertip
# ---------------------------------------------------------------------------


def test_track_fingertip_docstring_example():
    assert track_fingertip(0.5, 0.5, 1280, 720) == (640, 360)


def test_track_fingertip_top_left():
    assert track_fingertip(0.0, 0.0, WIDTH, HEIGHT) == (0, 0)


def test_track_fingertip_bottom_right_stays_on_screen():
    assert track_fingertip(1.0, 1.0, WIDTH, HEIGHT) == (WIDTH - 1, HEIGHT - 1)


def test_track_fingertip_returns_tuple_of_two_ints():
    result = track_fingertip(0.3, 0.7, WIDTH, HEIGHT)
    assert isinstance(result, tuple)
    assert len(result) == 2
    assert all(type(v) is int for v in result)


@pytest.mark.parametrize(
    ("x", "y"),
    [(-0.1, 0.5), (1.1, 0.5), (0.5, -0.1), (0.5, 1.1)],
)
def test_track_fingertip_out_of_range_coordinates_raise(x, y):
    with pytest.raises(ValueError):
        track_fingertip(x, y, WIDTH, HEIGHT)


@pytest.mark.parametrize(
    ("width", "height"),
    [(0, HEIGHT), (-1, HEIGHT), (WIDTH, 0), (WIDTH, -1)],
)
def test_track_fingertip_non_positive_dimensions_raise(width, height):
    with pytest.raises(ValueError):
        track_fingertip(0.5, 0.5, width, height)


@pytest.mark.parametrize(("x", "y"), [(math.nan, 0.5), (0.5, math.nan)])
def test_track_fingertip_nan_coordinates_raise(x, y):
    with pytest.raises(ValueError):
        track_fingertip(x, y, WIDTH, HEIGHT)


# ---------------------------------------------------------------------------
# detect_slice
# ---------------------------------------------------------------------------


def test_detect_slice_docstring_example():
    assert detect_slice((0, 50), (100, 50), (50, 50), 20, 10) is True


def test_detect_slice_miss():
    assert detect_slice((0, 50), (100, 50), (50, 100), 20, 10) is False


def test_detect_slice_too_slow():
    assert detect_slice((0, 50), (5, 50), (3, 50), 20, 10) is False


def test_detect_slice_movement_exactly_min_speed_counts():
    # 이동 거리 10 == min_speed 10 이면 속도 조건을 통과한다.
    assert detect_slice((0, 50), (10, 50), (5, 50), 20, 10) is True


def test_detect_slice_segment_stops_short_of_fruit():
    # 무한 직선이라면 맞지만, 선분 끝(20, 50)에서 중심까지 거리가 30 > 20 이다.
    assert detect_slice((0, 50), (20, 50), (50, 50), 20, 10) is False


def test_detect_slice_tangent_is_not_a_hit():
    # 가장 가까운 거리 == 반지름 이면 strict < 비교라서 False.
    assert detect_slice((0.0, 0.0), (100.0, 0.0), (50.0, 20.0), 20.0, 10) is False


def test_detect_slice_diagonal_hit():
    assert detect_slice((0, 0), (100, 100), (50, 50), 5, 10) is True


def test_detect_slice_stationary_inside_fruit_with_zero_min_speed():
    assert detect_slice((50, 50), (50, 50), (55, 50), 20, 0) is True


def test_detect_slice_stationary_with_positive_min_speed():
    assert detect_slice((50, 50), (50, 50), (55, 50), 20, 1) is False


def test_detect_slice_accepts_lists_and_ints():
    assert detect_slice([0, 50], [100, 50], [50, 50], 20, 10) is True
    assert detect_slice((0.0, 50.0), (100.0, 50.0), (50.0, 50.0), 20.0, 10.0) is True


def test_detect_slice_returns_builtin_bool():
    assert type(detect_slice((0, 50), (100, 50), (50, 50), 20, 10)) is bool
    assert type(detect_slice((0, 50), (100, 50), (50, 100), 20, 10)) is bool


@pytest.mark.parametrize("radius", [0, -1, math.nan, math.inf])
def test_detect_slice_invalid_radius_raises(radius):
    with pytest.raises(ValueError):
        detect_slice((0, 50), (100, 50), (50, 50), radius, 10)


@pytest.mark.parametrize("min_speed", [-1, math.nan, math.inf])
def test_detect_slice_invalid_min_speed_raises(min_speed):
    with pytest.raises(ValueError):
        detect_slice((0, 50), (100, 50), (50, 50), 20, min_speed)


def test_detect_slice_zero_min_speed_is_allowed():
    assert detect_slice((0, 50), (100, 50), (50, 50), 20, 0) is True


# ---------------------------------------------------------------------------
# save_high_score
# ---------------------------------------------------------------------------


@pytest.fixture
def score_file(tmp_path):
    # 레포 폴더에 highscore.json이 생기지 않도록 임시 경로를 사용한다.
    return tmp_path / "highscore.json"


def _read(path):
    return json.loads(path.read_text(encoding="utf-8"))


def test_save_high_score_docstring_example(score_file):
    assert save_high_score(100, path=str(score_file)) is True


def test_save_high_score_writes_score_and_today(score_file):
    save_high_score(100, path=str(score_file))
    assert _read(score_file) == {"score": 100, "date": date.today().isoformat()}


def test_save_high_score_higher_score_overwrites(score_file):
    save_high_score(100, path=str(score_file))
    assert save_high_score(150, path=str(score_file)) is True
    assert _read(score_file)["score"] == 150


def test_save_high_score_lower_score_is_not_saved(score_file):
    save_high_score(100, path=str(score_file))
    assert save_high_score(50, path=str(score_file)) is False
    assert _read(score_file)["score"] == 100


def test_save_high_score_equal_score_is_not_saved(score_file):
    save_high_score(100, path=str(score_file))
    assert save_high_score(100, path=str(score_file)) is False
    assert _read(score_file)["score"] == 100


def test_save_high_score_zero_on_first_save(score_file):
    assert save_high_score(0, path=str(score_file)) is True
    assert _read(score_file)["score"] == 0


def test_save_high_score_negative_raises(score_file):
    with pytest.raises(ValueError):
        save_high_score(-1, path=str(score_file))
    assert not score_file.exists()


@pytest.mark.parametrize(
    "content",
    ["not json", '{"score": "100"}', "[100]", '{"date": "2026-01-01"}'],
)
def test_save_high_score_invalid_file_is_overwritten(score_file, content):
    # 깨졌거나 형식이 맞지 않는 파일은 기록 없음으로 보고 새 점수로 덮어쓴다.
    score_file.write_text(content, encoding="utf-8")
    assert save_high_score(10, path=str(score_file)) is True
    assert _read(score_file)["score"] == 10
