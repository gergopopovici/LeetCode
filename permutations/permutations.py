from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(current_perm):
            if len(current_perm) == len(nums):
                res.append(current_perm[:])
                return 
            for n in nums:
                if n not in current_perm:
                    current_perm.append(n)
                    backtrack(current_perm)
                    current_perm.pop()
        backtrack([])
        return res

my_solution = Solution()
res = my_solution.permute(nums=[1,2,3])
for i in res:
    print(i, end=" ")