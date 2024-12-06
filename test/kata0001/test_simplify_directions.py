import pytest

from src.kata0001.simplify_directions import simplify_directions


def test_removes_single_north_south_cancellation():
    test_input = ["NORTH", "SOUTH", "WEST"]
    assert simplify_directions(test_input) == ["WEST"]

    test_input = ["SOUTH", "NORTH", "EAST"]
    assert simplify_directions(test_input) == ["EAST"]


def test_removes_single_east_west_cancellation():
    test_input = ["NORTH", "EAST", "WEST"]
    assert simplify_directions(test_input) == ["NORTH"]

    test_input = ["WEST", "EAST", "SOUTH"]
    assert simplify_directions(test_input) == ["SOUTH"]


def test_removes_multiple_north_south_cancellations():
    test_input = ["NORTH", "SOUTH", "WEST", "SOUTH", "NORTH"]
    assert simplify_directions(test_input) == ["WEST"]

    test_input = ["EAST", "SOUTH", "SOUTH", "NORTH",
                  "NORTH", "NORTH", "SOUTH"]
    assert simplify_directions(test_input) == ["EAST"]


def test_removes_multiple_east_west_cancellations():
    test_input = ["NORTH", "EAST", "WEST", "WEST", "EAST"]
    assert simplify_directions(test_input) == ["NORTH"]

    test_input = ["WEST", "EAST", "SOUTH", "EAST",
                  "WEST", "EAST", "WEST"]
    assert simplify_directions(test_input) == ["SOUTH"]


def test_simplifies_while_retaining_multiple_moves_in_same_direction():
    test_input = ["NORTH", "EAST", "WEST", "SOUTH", "EAST",
                  "SOUTH", "EAST", "NORTH"]
    assert simplify_directions == ["EAST", "EAST"]

    test_input = ["EAST", "NORTH", "SOUTH", "SOUTH", "WEST",
                  "SOUTH", "NORTH", "EAST", "WEST", "SOUTH"]
    assert simplify_directions == ["SOUTH", "SOUTH"]

    test_input = ["WEST", "WEST", "WEST", "NORTH", "NORTH",
                  "EAST", "SOUTH", "SOUTH", "SOUTH", "WEST"]
    assert simplify_directions == ["WEST", "WEST", "WEST",
                                   "SOUTH", "SOUTH"]
    
    test_input = ["NORTH", "NORTH", "EAST", "SOUTH", "EAST",
                  "WEST", "NORTH"]
    assert simplify_directions == ["NORTH", "NORTH", "EAST"]