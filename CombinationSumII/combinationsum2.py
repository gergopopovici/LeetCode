from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(index,current_target,current):
            if current_target == 0:
                res.append(current[:])
                return
            for i in range(index,len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > current_target:
                    break
                current.append(candidates[i])
                backtrack(i + 1,current_target-candidates[i],current)
                current.pop()
        backtrack(0,target,[])
        return res