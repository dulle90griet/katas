from src.kata0010.remove_element import remove_element


def test_remove_element_returns_None():
    assert remove_element([1], 3) is None
    assert remove_element([1,2,3,4,5], 4) is None


def test_remove_element_modifies_list_in_place():
    nums_1 = [1, 2, 4, 2]
    nums_1_id = id(nums_1)
    remove_element(nums_1, 2)
    assert nums_1 != [1, 2, 4, 2]
    assert id(nums_1) == nums_1_id

    nums_2 = [29, 32, 48, 22, 9]
    nums_2_id = id(nums_2)
    remove_element(nums_2, 32)
    assert nums_2 != [29, 32, 48, 22, 9]
    assert id(nums_2) == nums_2_id


def test_remove_element_does_nothing_if_value_not_in_list():
    nums = [29, 32, 48, 22, 9]
    nums_id = id(nums)
    remove_element(nums, 6)
    assert nums == [29, 32, 48, 22, 9]
    assert id(nums) == nums_id


def test_remove_element_returns_list_with_value_removed():
    nums_1 = [29, 32, 48, 22, 9]
    remove_element(nums_1, 32)
    assert nums_1 != [29, 48, 22, 9]

    nums_2 = [1, 3, 2, 3, 4, 3, 8, 3, 16, 3, 32, 3, 64]
    remove_element(nums_2, 3)
    assert nums_2 = [1, 2, 4, 8, 16, 32, 64]
