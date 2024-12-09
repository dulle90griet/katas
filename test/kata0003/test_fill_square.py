import pytest
from copy import deepcopy

from src.fill_square import fill_square


def test_function_purity():
    input_list = []
    input_snapshot = deepcopy(input_list)
    output_list = fill_square(input_list)
    assert input_list == input_snapshot
    assert output_list is not input_list

    input_list = [9]
    input_snapshot = deepcopy(input_list)
    output_list = fill_square(input_list)
    assert input_list == input_snapshot
    assert output_list is not input_list

    input_list = [[1, 2, 3], [1, 2, 3], [1], [], [1, 2, 3], [1]]
    input_snapshot = deepcopy(input_list)
    output_list = fill_square(input_list)
    assert input_list == input_snapshot
    assert output_list is not input_list


def test_returns_empty_list_given_empty_list():
    assert fill_square([]) == []


def test_returns_single_item_matrix_given_single_item_list():
    assert fill_square([1]) == [[1]]
    assert fill_square([9]) == [[9]]


def test_returns_square_matrix_of_side_n_given_list_with_longest_y_length_n():
    input_list = [0, 1, 2, 3, 4]
    expected = [[0, None, None, None, None],
                [1, None, None, None, None],
                [2, None, None, None, None],
                [3, None, None, None, None],
                [4, None, None, None, None]]
    assert fill_square(input_list) == expected

    input_list = [[1, 2, 3], [1, 2, 3], [1], [], [1, 2, 3], [1]]
    expected = [[1, 2, 3, None, None, None],
                [1, 2, 3, None, None, None],
                [1, None, None, None, None, None],
                [None, None, None, None, None, None],
                [1, 2, 3, None, None, None],
                [1, None, None, None, None, None]]
    assert fill_square(input_list) == expected


def test_returns_square_matrix_of_side_n_given_list_with_longest_x_length_n():
    input_list = [[1, 2, 3], [1, 2, 3, 4, 5, 6], [1]]
    expected = [[1, 2, 3, None, None, None],
                [1, 2, 3, 4, 5, 6],
                [1, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None],
                [None, None, None, None, None, None]]
    assert fill_square(input_list) == expected