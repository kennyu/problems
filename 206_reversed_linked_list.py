from typing import Optional
from helper import ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return
        if head.next is None:
            return head
        curr = head
        next = head.next
        while next is not None:
            temp = curr
            curr = next
            next = next.next
            curr.next = temp
        head.next = None
        return curr

    def createLinkedList(self, arr):
        if len(arr) < 1:
            return None
        curr = ListNode(arr[0])
        head = curr
        for elem in arr[1:]:
            next = ListNode(elem)
            curr.next = next
            curr = next
        return head

# Test Cases
l1 = [1,2,3,4,5]

s = Solution()
print(ListNode.toList(s.createLinkedList(l1)))
h = s.reverseList(s.createLinkedList(l1))
print(ListNode.toList(h))
