from typing import List
import heapq
import unittest
case = unittest.TestCase()

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict()
        for i in nums:
            if i not in count:
                count[i] = 0
            count[i] += 1

        # prepopulate heap with first k elements
        heap = []
        iterable = iter(count.items())
        for _ in range(k):
            num, count = next(iterable)
            heap.append((count, num))
        heapq.heapify(heap)

        # iterate through rest of list and replace heap as needed
        for num, count in iterable:
            if count > heap[0][0]:
                # heapq.heappop(heap)
                # heapq.heappush(heap, (count, num))
                heapq.heapreplace(heap, (count, num))

        return [num for _, num in heap]

s = Solution()
case.assertCountEqual(s.topKFrequent([3,2,2,1,1,1], 2), [1,2])
case.assertCountEqual(s.topKFrequent([1], 1), [1])
