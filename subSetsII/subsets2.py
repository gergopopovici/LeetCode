from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(index,current):
            res.append(current[:])
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                current.append(nums[i])
                backtrack(i+1,current)
                current.pop()
        backtrack(0,[])
        return res


