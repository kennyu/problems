from typing import Optional
from helper import TreeNode

class Solution:
    def invertTree_recursive_dfs(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if node is None:
                return
            temp_left = node.left
            node.left = node.right
            node.right = temp_left
            invert(node.left)
            invert(node.right)
        invert(root)
        return root
