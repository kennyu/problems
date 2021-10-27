from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

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