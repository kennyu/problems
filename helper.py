from typing import List
from enum import Enum

class D(Enum):
    # l = "Ⓛ"
    # r = "Ⓡ"
    l = "←"
    r = "→"

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def fromList(lst):
        """ https://github.com/shurane/problems/blob/master/leetcode-clackamas/helpers.py """
        """ https://github.com/shurane/problems/blob/master/leetcode-clackamas/helpers.tests.py """
        if not lst:
            return None

        root = TreeNode(lst[0])
        tree = [root]

        for i in range(1, len(lst)):
            node = None
            if lst[i] is not None:
                node = TreeNode(lst[i])
            tree.append(node)
            parent = (i-1) // 2

            if node is None or tree[parent] is None:
                continue

            if i % 2 == 1:
                tree[parent].left = node
            else:
                tree[parent].right = node
        return root

    def __repr__(self, name=""):
        return TreeNode.print(self, name=name)

    @staticmethod
    def print(node, name="", indent=2):
        if not node:
            return "TreeNode(empty)"

        s = f"TreeNode({name})\n{node.val}\n"
        stack = [
            (indent, node.right, D.r),
            (indent, node.left, D.l)
        ]
        while stack:
            i, n, d = stack.pop()

            if not n: continue

            v = str(n.val) if n else "None"
            s += " " * (i-indent) + "└" + " " * (indent - 1) + v + f" {d.value}" + "\n"

            stack.append((i + indent, n.right, D.r))
            stack.append((i + indent, n.left, D.l))

        return s.strip()

    def __eq__(self, q) -> bool:
        p = self
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

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode

    def listify(self):
        return ListNode.toList(self)

    @staticmethod
    def toList(node):
        arr = []
        while node is not None:
            arr.append(node.val)
            node = node.next
        return arr

    @staticmethod
    def fromList(arr: List):
        if not arr:
            return None

        curr = ListNode(arr[0])
        head = curr
        for elem in arr[1:]:
            nextNode = ListNode(elem)
            curr.next = nextNode
            curr = nextNode
        return head