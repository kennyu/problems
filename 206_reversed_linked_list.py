from typing import List, Optional
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

s = Solution()

# Test Cases
assert s.reverseList(None) is None
t1 = ListNode(1)
assert s.reverseList(t1).listify() == [1]
t2 = ListNode.fromList([1,2,3,4,5])
assert s.reverseList(t2).listify() == [5,4,3,2,1]
t3 = ListNode.fromList([5,4,3,2,1])
assert s.reverseList(t3).listify() == [1,2,3,4,5]
