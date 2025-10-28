from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    dummy = head = ListNode(None)

    while True:
        for i in range(len(lists)-1, -1, -1):
            if not lists[i]:
                lists.pop(i)
        if not lists:
            break
            
        lowest = min(lists, key=lambda x: x.val)
        min_idx = lists.index(lowest)
        head.next = ListNode(lists[min_idx].val)
        head = head.next
        lists[min_idx] = lists[min_idx].next
    
    return dummy.next
