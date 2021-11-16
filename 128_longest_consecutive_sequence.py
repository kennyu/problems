from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_count = 0
        while s:
            n = next(iter(s))
            count = 1
            ascending = n + 1
            while ascending in s:
                s.remove(ascending)
                count += 1
                ascending += 1
            descending = n - 1
            while descending in s:
                s.remove(descending)
                count += 1
                descending -= 1
            s.remove(n)
            max_count = max(count,max_count)
        return max_count
