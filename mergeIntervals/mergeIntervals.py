from typing import List


class Solution:
 def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    """
    def get_start_time(interval):
        return interval[0]
    intervals.sort(key=get_start_time)
    """
    intervals.sort(key = lambda x: x[0])
    merged = []
    for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
    return merged

my_solution = Solution()
res = my_solution.merge(intervals = [[1,3],[2,6],[8,10],[15,18]])
for i in res:
    print(i,end=" ")