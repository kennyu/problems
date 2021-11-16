from helper import TreeNode
from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = -1000000000000
        def maxPathSumHelper(node):
            nonlocal maxSum
            if node is None:
                return 0
            left_max = maxPathSumHelper(node.left)
            right_max = maxPathSumHelper(node.right)
            connected_max = left_max + node.val + right_max
            non_connected_max = node.val + max(0, left_max, right_max)
            maxSum = max(maxSum, connected_max, non_connected_max)
            return non_connected_max
        maxPathSumHelper(root)
        return maxSum

s = Solution()
t1 = TreeNode.fromList([-10,9,20,None,None,15,7])
assert s.maxPathSum(t1) == 42
t2 = TreeNode.fromList([1,2,3])
assert s.maxPathSum(t2) == 6
