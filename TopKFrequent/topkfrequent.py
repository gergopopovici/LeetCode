from collections import Counter
from typing import List
import heapq



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        min_heap = []
        heapq.heapify(min_heap)
        for num,count in freq_map.items():
            heapq.heappush(min_heap, (count, num))
            if len(min_heap) > k :
                heapq.heappop(min_heap)
        res = []
        while min_heap :
            count, num = heapq.heappop(min_heap)
            res.append(num)
        return res[::-1]

my_solution = Solution()
result = my_solution.topKFrequent(nums = [1,1,1,2,2,3], k = 2)
for i in result:
    print(i, end=" ")