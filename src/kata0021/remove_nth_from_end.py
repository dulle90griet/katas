# Definition for singly-linked list is as follows:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def remove_nth_from_end(self, head, n: int):    # where `head` is a ListNode
    traversed = []
    cur_node = head

    while cur_node:
        traversed.append(cur_node)
        cur_node = cur_node.next
    
    # check n is in bounds
    if n == 0 or n > len(traversed):
        return head
    # remove from len == 1 list
    elif len(traversed) == 1:
        head = None
    # remove from end of list
    elif n == 1:
        traversed[-2].next = None
    # remove from start of list
    elif n == len(traversed):
        head = head.next
    # remove from middle of list
    else:
        traversed[-(n+1)].next = traversed[-(n-1)]

    return head
