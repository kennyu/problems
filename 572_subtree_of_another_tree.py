from typing import Optional
from helper import TreeNode

class Solution:
    def isSubtree_v1(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        root_nodes = [root]
        while root_nodes:
            node = root_nodes.pop()
            if not node:
                continue
            if node.val == subRoot.val:
                if equal(node, subRoot):
                    return True
            root_nodes.append(node.left)
            root_nodes.append(node.right)
        return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Function to hash a tree
        def hash_subtree(node):
            if node is None:
                return hash(None)
            left = hash_subtree(node.left)
            right = hash_subtree(node.right)
            hash_val = hash(5*node.val + 7*left + 17*right)
            return hash_val
        # Hash of the subtree
        subTreeHash = hash_subtree(subRoot)
        # Find is subtree hash is root tree
        subTree_found = False
        def helper(node):
            nonlocal subTreeHash
            nonlocal subTree_found
            if node is None:
                return hash(None)
            left = helper(node.left)
            right = helper(node.right)
            hash_val = hash(5*node.val + 7*left + 17*right)
            if hash_val == subTreeHash:
                subTree_found = True
            return hash_val
        helper(root)
        return subTree_found

def equal(p,q) -> bool:
    if q is None:
        return p is None
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
t1 = (TreeNode.fromList([1,2,3]), TreeNode(1))
assert s.isSubtree(*t1) == False
assert s.isSubtree_v1(*t1) == False
t2 = (TreeNode.fromList([3,4,5,1,None,2]), TreeNode.fromList([4,1]))
assert s.isSubtree(*t2) == True
assert s.isSubtree_v1(*t2) == True
t3 = (TreeNode.fromList([1,1]), TreeNode(1))
assert s.isSubtree(*t3) == True
assert s.isSubtree_v1(*t3) == True
t4 = (TreeNode.fromList([1,1,1,]), TreeNode.fromList([1,None,1]))
assert s.isSubtree(*t4) == False
assert s.isSubtree_v1(*t4) == False
