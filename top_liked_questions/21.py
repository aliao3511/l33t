class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        first = l1
        second = l2
        dummy = ListNode(0)
        head = dummy
        while first and second:
            if first.val > second.val:
                val = second.val
                second = second.next
            else:
                val = first.val
                first = first.next
            head.next = ListNode(val)
            head = head.next
        if first:
            while first:
                head.next = ListNode(first.val)
                first = first.next
                head = head.next
        else:
            while second:
                head.next = ListNode(second.val)
                second = second.next
                head = head.next
        return dummy.next
