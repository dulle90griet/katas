# Definition for singly-linked list is as follows:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def remove_nth_from_end(self, head, n: int):    # where `head` is a ListNode
    head_keeper = ListNode(0, head)
    node_cutter = head_keeper

    # Advance the head pointer to establish the required space
    # between it and the cutter
    for _ in range(n):
        head = head.next
    
    # Move head and cutter pointers together until head passes the list end
    while head:
        head = head.next
        node_cutter = node_cutter.next

    # Redirect the node at the cutter pointer to make the cut
    node_cutter.next = node_cutter.next.next

    # Return the new head
    return head_keeper.next