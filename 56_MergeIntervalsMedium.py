"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """ O(n*log n) """
        pointer = 1
        intervals.sort()
        ans = []
        now_start = intervals[0][0]
        now_end = intervals[0][1]
        while pointer < len(intervals):
            start = intervals[pointer][0]
            end = intervals[pointer][1]
            if start <= now_end:
                now_end = max(end, now_end) 
                pointer += 1 
            else:
                ans.append([now_start, now_end])
                now_start = start
                now_end = end
                pointer += 1
        ans.append([now_start, now_end])
        return ans
