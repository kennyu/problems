from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        left = 0
        right = len(nums)-1

        while left < right:
            pivot = (right + left) // 2
            if nums[pivot] < nums[pivot-1]:
                break
            if nums[pivot+1] < nums[pivot]:
                pivot += 1
                break
            if nums[left] < nums[pivot]:
                left = pivot + 1
            else:
                right = pivot - 1
        lresult = self.binary_search(nums, target, 0, pivot)
        rresult = self.binary_search(nums, target, pivot, len(nums) - 1)
        # print("pivot", pivot, "lresult", lresult, "rresult", rresult)
        return max(lresult, rresult)

    def binary_search(self, nums: List[int], target: int, lo: int, hi: int):
        while lo <= hi:
            mid = (hi + lo) // 2
            # print(f"lo {lo:2} mid {mid:2} hi {hi:2} ")
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

    def search2(self, nums: List[int], target: int) -> int:
        # see https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14437/Python-binary-search-solution-O(logn)-48ms
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            # print(f"lo {lo:2} mid {mid:2} hi {hi:2} ")
            if nums[mid] == target:
                return mid
            elif nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1

        # print("didn't find result")
        return -1

s = Solution()

assert s.search([4,5,6,7,0,1,2],0) == 4
assert s.search([4,5,6,7,0,1,2],3) == -1
assert s.search([1],0) == -1

lst = list(range(32))

for i in lst:
    rotated = lst[~i+1:] + lst[0:~i+1]
    # print(f"{i:2}", rotated)
    assert s.search(rotated, 0) == i
    assert s.search2(rotated, 0) == i