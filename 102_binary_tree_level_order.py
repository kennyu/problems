from typing import Optional, List
from helper import TreeNode

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return_arr = []
        levels_seen = set()
        def traverse(level, node):
            if node is None:
                return
            elif level in levels_seen:
                return_arr[level].append(node.val)
            else:
                return_arr.append([node.val])
                levels_seen.add(level)
            traverse(level+1, node.left)
            traverse(level+1, node.right)
        traverse(0,root)
        return return_arr
