from src.kata0007.data_munging import find_smallest_spread

def test_find_smallest_spread_outputs_smallest_spread(capsys):
    find_smallest_spread()
    
    stdout, _ = capsys.readouterr()

    assert "Day 14 saw the smallest temperature spread, at 2 degrees." in stdout