from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums)-1
        # Edge case
        if nums[lo] < nums[hi] or hi == lo:
            return nums[lo]
        # Pivot case
        while lo < hi:
            mid = int((hi-lo) / 2 + lo)
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid+1] < nums[mid]:
                return nums[mid+1]

            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[lo]:
                hi = mid - 1

# Test Cases
l1 = [3,4,5,1,2]
l2 = [4,5,6,7,0,1,2]
l3 = [11,13,15,17]

s = Solution()
assert(s.findMin(l1) == 1)
assert(s.findMin(l2) == 0)
assert(s.findMin(l3) == 11)


