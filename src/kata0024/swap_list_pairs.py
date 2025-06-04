# Definition for singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def swap_list_pairs(head):      # where `head` is a ListNode
    head_holder = ListNode(0, head)
    rear = head_holder

    while head and head.next:
        swap_A = head
        swap_B = head.next

        rear.next = swap_B
        swap_A.next = swap_B.next
        swap_B.next = swap_A

        rear = swap_A
        head = swap_A.next
    
    return head_holder.next
