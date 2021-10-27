from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp_product = [[nums[0], min( 1, nums[0] ) ]]
        for idx in range(1,len(nums)):
            value = nums[idx]
            dp_product.append( [ max(value, value*dp_product[idx-1][0], value*dp_product[idx-1][1]), 1 ] )
            if value < 0 or dp_product[idx-1][1] < 0:
                dp_product[idx][1] = min(value, value*dp_product[idx-1][0], value*dp_product[idx-1][1])
        return max( dp_product )[0]

# Test Cases
l1 = [2,3,-2,4]
l2 = [-2, 0, -1]
l3 = [2, 3, -2, 4, -2]
l4 = [2, 3, -2, 4, 0, -2]
l5 = [2, -3, 2, -4, 0, -3, -20]
l6 = [2, -3, 2, -4, 0, -3, 20]
l7 = [-2,-3,-4,-5,-6,-7,-8]

s = Solution()
assert s.maxProduct(l1) == 6
assert s.maxProduct(l2) == 0
assert s.maxProduct(l3) == 96
assert s.maxProduct(l4) == 6
assert s.maxProduct(l6) == 48
assert s.maxProduct(l7) == 20160
