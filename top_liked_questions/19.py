class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        for i in range(n + 1):
            second = second.next
        while second:
            first = first.next
            second = second.next
        first.next = first.next.next
        return dummy.next
