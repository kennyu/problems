from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        return_arr = [intervals[0]]
        for i,j in intervals[1:]:
            start, end = return_arr[-1]
            if start <= i and i <= end:
                return_arr[-1][1] = max(j,return_arr[-1][1])
            else:
                return_arr.append([i,j])
        return return_arr
            

# Test Cases
l1 = [[1,3],[2,6],[8,10],[15,18]]
l2 = [[1,10],[2,9],[3,8],[4,7],[5,6]] # should reduce to [[1,10]], later intervals are completely inside [1,10]
l3 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7],[7,8],[8,9],[9,10]] # should reduce to [[1,10]], overlaps on edges
l4 = [[1,6],[2,7],[3,8],[4,9],[5,10]] # should reduce to [[1,10], overlaps by criss-crossing
l5 = [[1,2],[3,4],[5,6],[7,8],[9,10]] # stays the same
l6 = [[1,4], [0,4]]

s = Solution()
print(s.merge(l6))