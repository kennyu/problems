from typing import Optional
from helper import TreeNode

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        arr = [p,q]
        while len(arr) > 0:
            tree_node_p, tree_node_q = arr.pop(), arr.pop()
            if tree_node_p is None or tree_node_q is None:
                if tree_node_p != tree_node_q:
                    return False
                continue
            elif tree_node_p.val != tree_node_q.val:
                return False
            arr.append(tree_node_p.left)
            arr.append(tree_node_q.left)
            arr.append(tree_node_p.right)
            arr.append(tree_node_q.right)
        return True

s = Solution()
assert s.isSameTree(TreeNode(1), TreeNode(1)) == True

t1 = TreeNode.fromList([1,2,3,4,5,6,7])
t2 = TreeNode.fromList([1,2,None,4,5,None,None,6,7])

assert s.isSameTree(t1, t2) == False
