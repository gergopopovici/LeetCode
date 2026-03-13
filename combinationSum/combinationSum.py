from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, current_target,current_combo):
            if current_target == 0 :
                res.append(current_combo[:])
                return 
            if current_target < 0 or index == len(candidates):
                return
            current_combo.append(candidates[index])
            backtrack(index, current_target-candidates[index],current_combo)
            current_combo.pop()
            backtrack(index+1,current_target,current_combo)
        backtrack(0,target,[])
        return res


