from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        for idx, node in enumerate(lists):
            if node is not None:
                minheap.append((node.val,idx))
        heapq.heapify(minheap)
        head, curr = None, None
        while minheap:
            list_idx = minheap[0][1]
            next_node = lists[list_idx].next
            if next_node is not None:
                node = heapq.heappushpop( minheap, (next_node.val, list_idx))
            else:
                node = heapq.heappop( minheap )
            lists[list_idx] = lists[list_idx].next
            if head is None:
                head = ListNode(node[0])
                curr = head
            else:
                curr.next = ListNode(node[0])
                curr = curr.next
        return head
