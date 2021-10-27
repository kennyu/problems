from typing import List

class Solution:
    def findMin(self, nums: List[int], lo: int = 0, hi: int = None) -> int:
        if hi is None:
            hi = len(nums) - 1
        while lo < hi:
            mid = int((hi-lo) / 2 + lo)
            # print(f"lo {lo:2} mid {mid:2} hi {hi:2} ")
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            elif nums[mid+1] < nums[mid]:
                return nums[mid+1]

            if nums[mid] > nums[hi]:
                lo = mid + 1
            elif nums[mid] < nums[lo]:
                hi = mid - 1
            else:
                left = self.findMin(nums,lo,mid-1)
                right = self.findMin(nums,mid+1,hi)
                return min(left,right)
        return nums[lo]

s = Solution()

n = 16
# lst = [0 for i in range(n)] + [1 for i in range(n)]
# for i in range(n):
#     rotated = lst[~i+1:] + lst[0:~i+1]
#     # print(rotated)
#     assert s.findMin(rotated) == 0

lst = [1 for i in range(n * 2)]
for i in range(n*2):
    rotated = lst[:]
    rotated[i] = 0
    # print(rotated)
    assert s.findMin(rotated) == 0
