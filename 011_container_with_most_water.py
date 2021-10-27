from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        water_vol = 0
        i, j = 0, len(height)-1
        while i < j:
            water_vol = max(water_vol, (j-i)*min(height[i],height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water_vol
            

# Test cases
l1 = [1,8,6,2,5,4,8,3,7]
l2 = [1,1]
l3 = [4,3,2,1,4]
l4 = [1,2,1]

s = Solution()
assert( s.maxArea(l1) == 49 )
assert( s.maxArea(l2) == 1 )
assert( s.maxArea(l3) == 16 )
assert( s.maxArea(l4) == 2 )
