# Definition for singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def reverseKGroup(head, k: int):
    if k < 2:
        return head

    dummy = ListNode(0, head)
    rear = dummy

    nodes = 0
    while head:
        nodes += 1
        head = head.next

    cycles = nodes // k
    head = dummy.next

    for _ in range(cycles):
        circumference = head
        fore = head.next
        for __ in range(k-1):
            prev = circumference
            circumference = fore
            fore = fore.next

            circumference.next = prev
        head.next = fore
        rear.next = circumference

        head = fore
        rear = prev

    return dummy.next