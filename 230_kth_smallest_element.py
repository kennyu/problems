from typing import Optional
from helper import TreeNode

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        answer = None
        def inorder_traversal(node):
            nonlocal k
            nonlocal answer
            if not node or k < 0:
                return
            inorder_traversal(node.left)
            k -= 1
            if k == 0:
                k -= 1
                answer = node.val
            inorder_traversal(node.right)
        inorder_traversal(root)
        return answer

s = Solution()
t1 = TreeNode(1)
assert s.kthSmallest(t1,1) == 1
t2 = TreeNode.fromList([4,2,6,1,3,5,7])
assert s.kthSmallest(t2, 1) == 1
assert s.kthSmallest(t2, 2) == 2
assert s.kthSmallest(t2, 3) == 3
assert s.kthSmallest(t2, 4) == 4
assert s.kthSmallest(t2, 5) == 5
assert s.kthSmallest(t2, 6) == 6
assert s.kthSmallest(t2, 7) == 7
