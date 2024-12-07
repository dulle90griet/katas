import pytest

from src.kata0002.get_sub_square import get_sub_square


def test_returns_sub_square_with_zero_coords():
    matrix = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 4, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    result = get_sub_square(matrix, 0, 0)
    assert result == [
        [5, 3, 4],
        [6, 7, 2],
        [1, 9, 8]
    ]


def test_returns_sub_square_with_identical_non_zero_coords():
    matrix = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 4, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    result = get_sub_square(matrix, 3, 3)
    assert result == [
        [7, 4, 1],
        [8, 5, 3],
        [9, 2, 4]
    ]
    result = get_sub_square(matrix, 6, 6)
    assert result == [
        [2, 8, 4],
        [6, 3, 5],
        [1, 7, 9]
    ]


def test_returns_sub_square_with_non_identical_non_zero_coords():
    matrix = [
        [5, 3, 4, 6, 7, 8, 9, 1, 2],
        [6, 7, 2, 1, 9, 5, 3, 4, 8],
        [1, 9, 8, 3, 4, 2, 5, 6, 7],
        [8, 5, 9, 7, 4, 1, 4, 2, 3],
        [4, 2, 6, 8, 5, 3, 7, 9, 1],
        [7, 1, 3, 9, 2, 4, 8, 5, 6],
        [9, 6, 1, 5, 3, 7, 2, 8, 4],
        [2, 8, 7, 4, 1, 9, 6, 3, 5],
        [3, 4, 5, 2, 8, 6, 1, 7, 9]
    ]
    result = get_sub_square(matrix, 3, 5)
    assert result == [
        [9, 2, 4],
        [5, 3, 7],
        [4, 1, 9]
    ]
    result = get_sub_square(matrix, 0, 6)
    assert result == [
        [9, 6, 1],
        [2, 8, 7],
        [3, 4, 5]
    ]


@pytest.mark.skip
def test_returns_None_for_coords_out_of_bounds():
    pass