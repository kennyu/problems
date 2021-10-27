from typing import Optional
from helper import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def recursive_remove(node):
            if node.next is None:
                return n - 1
            else:
                return_val = recursive_remove(node.next)
                if return_val == 0:
                    node.next = node.next.next
                return return_val - 1
        return head if recursive_remove(head) != 0 else head.next

# Test Cases
s = Solution()

for i in range(1,10+1):
    before = list(range(10))
    lst = ListNode.fromList(before)
    after = ListNode.toList(s.removeNthFromEnd(lst, i))
    diff = set(before) - set(after)
    # print(diff, 10 - i)
    assert 10 - i in diff

l1 = ListNode.fromList([1,2,3,4,5])
l2 = ListNode.fromList([1])
assert ListNode.toList(s.removeNthFromEnd(l1, 2)) == [1,2,3,5]
assert ListNode.toList(s.removeNthFromEnd(l2, 1)) == []
