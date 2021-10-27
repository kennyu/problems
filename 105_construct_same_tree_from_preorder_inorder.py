from typing import List, Optional
from helper import TreeNode

class Solution:
    def buildTreeRecursive(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def buildTreeHelper(preorder: List[int], il, ir):
            if not preorder:
                return None

            val = preorder[0]
            split = inorder.index(val)
            il_left, il_right = il ,split
            ir_left, ir_right = split + 1, ir

            lefts = set(inorder[il_left:il_right])
            pleft = []
            pright = []
            for i in range(1, len(preorder)):
                elem = preorder[i]
                if elem in lefts:
                    pleft.append(elem)
                else:
                    pright.append(elem)

            node = TreeNode(val)
            node.left = buildTreeHelper(pleft, il_left, il_right)
            node.right = buildTreeHelper(pright, ir_left, ir_right)
            return node
        return buildTreeHelper(preorder, 0, len(inorder) - 1)

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        relations_map = dict()
        work_queue = [(0,len(preorder)-1 , 0 , len(inorder)-1)]
        def buildTreeHelper(pl, pr, il, ir):
            if il >= ir:
                return
            val = preorder[pl]
            pivot = inorder.index(val)
            for i in range(il,pivot):
                relations_map[inorder[i]] = (val, True)
            for j in range(pivot+1, ir+1):
                relations_map[inorder[j]] = (val, False)
            work_queue.append((pl + 1 , pl + 1 + pivot - 1 - il , il, pivot - 1))
            work_queue.append(( pr - ( ir - pivot - 1), pr, pivot + 1, ir ))
        while work_queue:
            buildTreeHelper(*work_queue.pop())
        nodes = dict()
        for child_val, (parent_val, is_to_left) in relations_map.items():
            child_node = nodes[child_val] if child_val in nodes else TreeNode(child_val)
            parent_node = nodes[parent_val] if parent_val in nodes else TreeNode(parent_val)
            if is_to_left is True:
                parent_node.left = child_node
            else:
                parent_node.right = child_node
            nodes[parent_val] = parent_node
            nodes[child_val] = child_node
        root_val = preorder[0]
        return nodes[root_val] if root_val in nodes else TreeNode(root_val)

s = Solution()
# Test Cases
t1 = TreeNode(4)
t1.left = TreeNode(2)
t1.right = TreeNode(6)
t1.left.left = TreeNode(1)
t1.left.right = TreeNode(3)
t1.right.left = TreeNode(5)
t1.right.right = TreeNode(7)

assert s.buildTree([4,2,1,3,6,5,7], [1,2,3,4,5,6,7]) == t1

t2 = TreeNode(1)
t2.right = TreeNode(2)
t2.right.right = TreeNode(3)
t2.right.right.right = TreeNode(4)
t2.right.right.right.right = TreeNode(5)
t2.right.right.right.right.right = TreeNode(6)
t2.right.right.right.right.right.right = TreeNode(7)

assert s.buildTree([1,2,3,4,5,6,7], [1,2,3,4,5,6,7]) == t2

t3 = TreeNode(7)
t3.left = TreeNode(6)
t3.left.left = TreeNode(5)
t3.left.left.left = TreeNode(4)
t3.left.left.left.left = TreeNode(3)
t3.left.left.left.left.left = TreeNode(2)
t3.left.left.left.left.left.left = TreeNode(1)

assert s.buildTree([7,6,5,4,3,2,1], [1,2,3,4,5,6,7]) == t3

# zig zag the tree
t4 = TreeNode(1)
t4.left = TreeNode(2)
t4.left.right = TreeNode(3)
t4.left.right.left = TreeNode(4)
t4.left.right.left.right = TreeNode(5)
t4.left.right.left.right.left = TreeNode(6)
t4.left.right.left.right.left.right = TreeNode(7)

assert s.buildTree([1,2,3,4,5,6,7],[2,4,6,7,5,3,1]) == t4

assert (t4 == t4) == True
assert (t4 == None) == False
assert (None == t4) == False

assert s.buildTree([-1],[-1]) == TreeNode(-1)