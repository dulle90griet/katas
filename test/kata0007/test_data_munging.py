from src.kata0007.data_munging import find_smallest_spread, find_smallest_goal_difference

def test_find_smallest_spread_outputs_smallest_spread(capsys):
    find_smallest_spread()
    
    stdout, _ = capsys.readouterr()

    assert "Day 14 saw the smallest temperature spread, at 2 degrees." in stdout


def test_find_smallest_goal_difference_outputs_smallest_difference(capsys):
    find_smallest_goal_difference()

    stdout, _ = capsys.readouterr()

    assert "Aston_Villa had the smallest difference (1) between 'for' and 'against' goals." in stdout