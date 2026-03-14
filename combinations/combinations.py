from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(index,current) :
            if k == len(current):
                res.append(current[:])
                return
            for i in range(index,n+1,1):
                current.append(i)
                backtrack(i+1,current)
                current.pop()
        backtrack(1,[])
        return res