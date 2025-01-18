import pandas as pd

from src.kata0007.data_munging import find_smallest_spread, find_smallest_goal_difference, find_min_diff_and_label


def test_find_min_diff_and_label_returns_expected_tuple_for_positive_diffs():
    test_df = pd.DataFrame.from_dict([
        {"label": 0, "a": 13, "b": 9},
        {"label": 1, "a": 27, "b": 2},
        {"label": 2, "a": 300, "b": 299}
    ])
    output = find_min_diff_and_label(test_df, "a", "b", "label")
    assert type(output) is tuple
    min_diff, label = output
    assert min_diff == 1
    assert label == 2


def test_find_min_diff_and_label_returns_expected_tuple_for_mixed_diffs():
    test_df = pd.DataFrame.from_dict([
        {"label": 0, "a": 13, "b": 27},
        {"label": 1, "a": 27, "b": 2},
        {"label": 2, "a": 299, "b": 300}
    ])
    min_diff, label = find_min_diff_and_label(test_df, "a", "b", "label")
    assert min_diff == 1
    assert label == 2


def test_find_smallest_spread_outputs_smallest_spread(capsys):
    find_smallest_spread()
    
    stdout, _ = capsys.readouterr()

    assert "Day 14 saw the smallest temperature spread, at 2 degrees." in stdout


def test_find_smallest_goal_difference_outputs_smallest_difference(capsys):
    find_smallest_goal_difference()

    stdout, _ = capsys.readouterr()

    assert "Aston_Villa had the smallest difference (1) between 'for' and 'against' goals." in stdout