from typing import List

class Solution:
    def merge_v1(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        return_arr = [intervals[0]]
        for i,j in intervals[1:]:
            start, end = return_arr[-1]
            if start <= i and i <= end:
                return_arr[-1][1] = max(j,return_arr[-1][1])
            else:
                return_arr.append([i,j])
        return return_arr

    def merge(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        curr = intervals[-1]
        for i in range(len(intervals)-1,0,-1):
            prev = intervals[i-1]
            if prev[1] >= curr[0]:
                prev[1] = curr[1]
                prev[0] = min(curr[0], prev[0])
                intervals.pop(i)
            curr = prev
        # print("intervals ", intervals)
        return intervals


# Test Cases
l1 = [[1,3],[2,6],[8,10],[15,18]]
l2 = [[1,10],[2,9],[3,8],[4,7],[5,6]] # should reduce to [[1,10]], later intervals are completely inside [1,10]
l3 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10]] # should reduce to [[1,10]], overlaps on edges
l4 = [[1,6],[2,7],[3,8],[4,9],[5,10]] # should reduce to [[1,10], overlaps by criss-crossing
l5 = [[1,2],[3,4],[5,6],[7,8],[9,10]] # stays the same
l6 = [[1,4], [0,4]]

s = Solution()
assert s.merge(l1) == [[1,6],[8,10],[15,18]]
assert s.merge(l2) == [[1,10]]
assert s.merge(l3) == [[1,10]]
assert s.merge(l4) == [[1,10]]
assert s.merge(l5) == [[1,2],[3,4],[5,6],[7,8],[9,10]]
assert s.merge(l6) == [[0,4]]