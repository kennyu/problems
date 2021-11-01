from typing import Optional
from helper import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = future = head
        while future and future.next:
            curr = curr.next
            future = future.next.next
            if curr == future:
                return True
        return False

# Test Cases
s = Solution()

# create cycle from a node that's ahead to a node that's behind
for i in range(19):
    for j in range(i+1):
        t = ListNode.fromList(range(19))
        # print(f"creating a cycle from {i:2} back to {j:2}: {t.listify()}")
        ahead = t
        behind = t

        for k in range(i):
            ahead = ahead.next
        for k in range(j):
            behind = behind.next

        # link the node that's ahead to the one that's behind, thus creating a cycle
        ahead.next = behind
        assert s.hasCycle(t) == True

t1 = ListNode.fromList([1,2,3,4,5])
t1.next.next.next.next = t1
t2 = ListNode.fromList([1,2,3,4,5])
assert s.hasCycle(t1) == True
assert s.hasCycle(t2) == False
