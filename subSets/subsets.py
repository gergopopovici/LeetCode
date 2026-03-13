from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, current_subset):
            if index == len(nums):
                res.append(current_subset[:])
                return
            current_subset.append(nums[index])
            backtrack(index+1,current_subset)
            current_subset.pop()
            backtrack(index+1,current_subset)
        backtrack(0,[])
        return res

my_solution = Solution()
res = my_solution.subsets(nums=[1,2,3])
for i in res :
    print(i, end=" ")