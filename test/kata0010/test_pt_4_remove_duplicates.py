from src.kata0010.pt_4_remove_duplicates import remove_duplicates

def test_r_d_modifies_list_in_place():
    nums = [1, 1, 2, 2, 3, 3, 3, 4, 5, 5]
    nums_id = id(nums)
    remove_duplicates(nums)
    assert id(nums) == nums_id

def test_r_d_removes_duplicates_and_returns_number_of_unique_elements():
    nums = [1, 1, 2]
    k = remove_duplicates(nums)
    assert nums[:k] == [1, 2]

    nums = [0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5]
    k = remove_duplicates(nums)
    assert nums[:k] == [0, 1, 2, 3, 4, 5]

    nums = [13, 17, 17, 27, 27, 27, 27, 1000, 2400, 2400, 9000]
    k = remove_duplicates(nums)
    assert nums[:k] == [13, 17, 27, 1000, 2400, 9000]

def test_r_d_leaves_list_unchanged_and_returns_orig_length_of_list_if_no_duplicates():
    nums = [1, 2, 3, 5, 8, 13, 21, 34]
    k = remove_duplicates(nums)
    assert nums[:k] == [1, 2, 3, 5, 8, 13, 21, 34]
