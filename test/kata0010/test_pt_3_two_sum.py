from src.kata0010.pt3_two_sum import two_sum

def test_two_sum_returns_list_of_two_ints():
    output = two_sum([1, 2, 3, 4, 5], 5)
    assert type(output) is list
    assert len(output) == 2
    assert type(output[0]) is int
    assert type(output[1]) is int

def test_two_sums_does_not_modify_input_list():
    nums_1 = [1, 2, 3]
    two_sum(nums_1, 3)
    assert nums_1 == [1, 2, 3]

    nums_2 = [10, 9, 8, 7, 6, 5]
    two_sum(nums_2, 14)
    assert nums_2 == [10, 9, 8, 7, 6, 5]

def test_indices_returned_by_two_sum_reference_numbers_summing_to_target():
    nums_1 = [1, 2, 3, 4, 5]
    output = two_sum(nums_1, 5)
    assert nums_1[output[0]] + nums_1[output[1]] == 5

    nums_2 = [32, 4096, 64, 2048, 128, 1024, 256, 512]
    output = two_sum(nums_2, 2304)
    assert nums_2[output[0]] + nums_2[output[1]] == 2304