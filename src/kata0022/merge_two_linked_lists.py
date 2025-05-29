# Definition for singly-linked list is as follows:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def merge_two_linked_lists(self, list1, list2):   # where `list1` and `list2` are ListNodes
    merge_head = ListNode(0, None)
    merge_cur = merge_head

    while list1 and list2:
        if list1.val <= list2.val:
            merge_cur.next = list1
            list1 = list1.next
        else:
            merge_cur.next = list2
            list2 = list2.next

        merge_cur = merge_cur.next

    # For some reason the below is faster than a ternary operator - why?
    if not list1:
        merge_cur.next = list2
    else:
        merge_cur.next = list1

    return merge_head