from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        curr, keep = intervals[-1], 1
        for i in range(len(intervals)-2,-1,-1):
            prev = intervals[i]
            if curr[0] >= prev[1]:
                keep += 1
                curr = prev
        answer = len(intervals) - keep
        return answer

s = Solution()

t1 = [[1,2],[1,2],[1,2]]
assert s.eraseOverlapIntervals(t1) == 2
t2 = [[1,2],[3,4],[5,6]]
assert s.eraseOverlapIntervals(t2) == 0
t3 = [[1,2],[2,3],[3,4]]
assert s.eraseOverlapIntervals(t3) == 0
t4 = [[1,2],[2,3],[3,4],[1,3]]
assert s.eraseOverlapIntervals(t4) == 1
