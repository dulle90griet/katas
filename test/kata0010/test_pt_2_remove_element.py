from src.kata0010.pt_2_remove_element import remove_element


def test_remove_element_modifies_list_in_place():
    nums_1 = [1, 2, 4, 2]
    nums_1_id = id(nums_1)
    k = remove_element(nums_1, 2)
    assert nums_1[:k] != [1, 2, 4, 2]
    assert id(nums_1) == nums_1_id

    nums_2 = [29, 32, 48, 22, 9]
    nums_2_id = id(nums_2)
    k = remove_element(nums_2, 32)
    assert nums_2[:k] != [29, 32, 48, 22, 9]
    assert id(nums_2) == nums_2_id


def test_remove_element_does_nothing_if_value_not_in_list():
    nums = [29, 32, 48, 22, 9]
    nums_id = id(nums)
    k = remove_element(nums, 6)
    assert nums[:k] == [29, 32, 48, 22, 9]
    assert id(nums) == nums_id


def test_remove_element_removes_all_instances_of_value_from_list():
    nums_1 = [29, 32, 48, 22, 9]
    k = remove_element(nums_1, 32)
    assert nums_1[:k] == [29, 48, 22, 9]

    nums_2 = [1, 3, 2, 3, 4, 3, 8, 3, 16, 3, 32, 3, 64]
    k = remove_element(nums_2, 3)
    assert nums_2[:k] == [1, 2, 4, 8, 16, 32, 64]


def test_remove_element_returns_number_of_elements_not_equal_to_value():
    nums_1 = [10, 20, 30, 40, 50, 60, 40]
    assert remove_element(nums_1, 40) == 5

    nums_2 = [19, 20, 21, 22, 23]
    assert remove_element(nums_2, 21) == 4


