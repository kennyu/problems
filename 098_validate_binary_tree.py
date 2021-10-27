from typing import Optional
from helper import TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        curr_val = -2147483649
        def inorder_traversal(node):
            nonlocal curr_val
            if node is None:
                return
            inorder_traversal(node.left)
            if curr_val is None:
                return
            if curr_val < node.val:
                curr_val = node.val
            else:
                curr_val = None
                return
            inorder_traversal(node.right)
        inorder_traversal(root)
        return False if curr_val is None else True

s = Solution()
t1 = TreeNode(2)
t1.left = TreeNode(1)
t1.right = TreeNode(3)
assert s.isValidBST(t1) == True

t2 = TreeNode(5)
t2.left = TreeNode(1)
t2.right = TreeNode(4)
t2.right.left = TreeNode(3)
t2.right.right = TreeNode(6)
assert s.isValidBST(t2) == False
