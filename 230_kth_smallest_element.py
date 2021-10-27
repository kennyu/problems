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