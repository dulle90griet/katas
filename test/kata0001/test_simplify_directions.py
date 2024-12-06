import pytest

from src.kata0001.simplify_directions import simplify_directions


def test_removes_single_north_south_cancellation():
    test_input = ["NORTH", "SOUTH", "WEST"]
    assert simplify_directions(test_input) == ["WEST"]

    test_input = ["SOUTH", "NORTH", "EAST"]
    assert simplify_directions(test_input) == ["EAST"]

@pytest.mark.skip
def test_removes_single_east_west_cancellation():
    pass

@pytest.mark.skip
def test_removes_multiple_north_south_cancellations():
    pass

@pytest.mark.skip
def test_removes_multiple_east_west_cancellations():
    pass

@pytest.mark.skip
def test_simplifies_while_retaining_multiple_moves_in_same_direction():
    pass