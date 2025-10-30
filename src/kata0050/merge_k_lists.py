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
            merged_dummy = merged_tail = ListNode()

            list_1_head = lists_to_merge[i]
            list_2_head = lists_to_merge[i+1] if i + 1 < len(lists_to_merge) else None

            while list_1_head and list_2_head:
                if list_1_head.val <= list_2_head.val:
                    merged_tail.next = ListNode(list_1_head.val)
                    merged_tail = merged_tail.next
                    list_1_head = list_1_head.next
                else:
                    merged_tail.next = ListNode(list_2_head.val)
                    merged_tail = merged_tail.next
                    list_2_head = list_2_head.next
            
            if list_1_head:
                merged_tail.next = list_1_head
            elif list_2_head:
                merged_tail.next = list_2_head

            merged_lists.append(merged_dummy.next)
        
        return merge_down(merged_lists)

    return merge_down(lists)
