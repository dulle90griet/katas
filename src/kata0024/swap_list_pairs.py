# Definition for singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def swap_list_pairs(head):      # where `head` is a ListNode
    if head is None or head.next is None:
        return head

    head_keeper = ListNode(0, head)
    rear = head_keeper
    front = head.next

    while front:
        swap_A = rear.next
        swap_B = front
        swap_next = swap_B.next

        rear.next = swap_B
        swap_B.next = swap_A
        swap_A.next = swap_next

        rear = rear.next.next
        if swap_next:
            front = swap_next.next
        else:
            break

    return head_keeper.next
