from src.kata0009.merge_sorted_lists import merge

def test_merge_returns_None():
    result = merge([1,2,3,0,0,0], 3, [1,2,3], 3)
    assert result is None

def test_merge_modifies_list_in_place():
    list1 = [1,2,3,0,0,0]
    list2 = [1,2,3]

    merge(list1, 3, list2, 3)

    assert list1 == [1,1,2,2,3,3]

def test_merge_merges_lists_with_all_lower_list_2():
    list1 = [4,5,6,0,0,0]
    list2 = [1,2,3]
    merge(list1, 3, list2, 3)
    assert list1 == [1,2,3,4,5,6]

    list1 = [4,5,6,7,8,9,10000,0,0,0]
    list2 = [1,2,3]
    merge(list1, 7, list2, 3)
    assert list1 == [1,2,3,4,5,6,7,8,9,10000]

def test_merge_merges_lists_with_all_higher_list_2():
    list1 = [1,2,3,0,0,0]
    list2 = [4,5,6]
    merge(list1, 3, list2, 3)
    assert list1 == [1,2,3,4,5,6]

    list1 = [2000, 4000, 0, 0, 0, 0]
    list2 = [4001, 4002, 4003, 100000]
    merge(list1, 2, list2, 4)
    assert list1 == [2000, 4000, 4001, 4002, 4003, 100000]

def test_merge_merges_lists_with_mixed_distribution():
    list1 = [1, 4, 9, 0, 0, 0]
    list2 = [2, 6, 20]
    merge(list1, 3, list2, 3)
    assert list1 == [1, 2, 4, 6, 9, 20]

    list1 = [2, 6, 12, 0, 0, 0]
    list2 = [1, 4, 8]
    merge(list1, 3, list2, 3)
    assert list1 == [1, 2, 4, 6, 8, 12]

    list1 = [4, 7, 12, 27, 28, 0, 0]
    list2 = [8, 26]
    merge(list1, 5, list2, 2)
    assert list1 == [4, 7, 8, 12, 26, 27, 28]

def test_merge_merges_list_with_length_1():
    list1 = [5, 0, 0, 0, 0]
    list2 = [2, 4, 6, 8]
    merge(list1, 1, list2, 4)
    assert list1 == [2, 4, 5, 6, 8]

    list1 = [100, 200, 300, 0]
    list2 = [201]
    merge(list1, 3, list2, 1)
    assert list1 == [100, 200, 201, 300]

def test_merge_merges_list_with_length_0():
    list1 = [0]
    list2 = [1]
    merge(list1, 0, list2, 1)
    assert list1 == [1]

    list1 = [1]
    list2 = []
    merge(list1, 1, list2, 0)
    assert list1 == [1]