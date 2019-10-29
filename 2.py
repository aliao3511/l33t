import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        carry = 0
        head = ListNode(0)
        current = head
        while node1 or node2:
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            sum = val1 + val2 + carry
            carry = sum // 10
            current.next = ListNode(sum % 10)
            current = current.next
            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None
        if carry > 0:
            current.next = ListNode(carry)
        return head.next