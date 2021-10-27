from typing import List
import itertools
import timeit

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        counter_bag = {}
        for value in nums:
            if value in counter_bag:
                if counter_bag[value] < 3:
                    counter_bag[value] += 1
            else:
                counter_bag[value] = 1
        reduced_nums = []
        for value in counter_bag:
            reduced_nums.extend([value]*counter_bag[value])
        
        bag = dict()
        for idx, value in enumerate(reduced_nums):
            if value in bag:
                if len(bag[value]) < 3:
                    bag[value].append(idx)
            else:
                bag[value] = [idx]
                
        return_set = set()
        reduced_nums = []
        for value in bag:
            reduced_nums.extend(len(bag[value])*[value])

        for i in range(len(reduced_nums)-1):
            for j in range(i+1, len(reduced_nums)):
                target = 0 - reduced_nums[i] - reduced_nums[j]
                if target in bag:
                    if len( set( [i,j] + bag[target] )) >= 3:
                        for k in bag[target]:
                            if k not in [i,j]:
                                return_set.add(tuple(sorted(map(lambda x: reduced_nums[x],[i,j,k]))))
                                
        return return_set

s = Solution()

l1 = [0,0,0,0,0,0,0,0,0,0]
l2 = list(itertools.chain(*[l1 for i in range(10)]))
l23 = list(itertools.chain(*[l1 for i in range(700)]))
l4 = [-1,0,1,2,-1,-4]

print(s.threeSum(l1))
# for i in range(1,30):
#     lst = list(itertools.chain(*[l1 for _ in range(i)]))
#     t = timeit.Timer(lambda: s.threeSum(lst))
#     print(len(lst), t.timeit(1))