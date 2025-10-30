from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    def merge_down(lists_to_merge):
        if len(lists_to_merge) == 0:
            return None
        if len(lists_to_merge) == 1:
            return lists_to_merge[0]

        merged_lists = []

        for i in range(0, len(lists_to_merge), 2):
            merged_dummy = merged_head = ListNode()

            list_1_head = lists_to_merge[i]
            list_2_head = lists_to_merge[i+1] if i+1 < len(lists_to_merge) else None

            while list_1_head or list_2_head:
                if list_2_head is None:
                    merged_head.next = ListNode(list_1_head.val)
                    merged_head = merged_head.next
                    list_1_head = list_1_head.next
                elif list_1_head is None:
                    merged_head.next = ListNode(list_2_head.val)
                    merged_head = merged_head.next
                    list_2_head = list_2_head.next
                elif list_1_head.val <= list_2_head.val:
                    merged_head.next = ListNode(list_1_head.val)
                    merged_head = merged_head.next
                    list_1_head = list_1_head.next
                else:
                    merged_head.next = ListNode(list_2_head.val)
                    merged_head = merged_head.next
                    list_2_head = list_2_head.next

            merged_lists.append(merged_dummy.next)
        
        return merge_down(merged_lists)

    return merge_down(lists)
