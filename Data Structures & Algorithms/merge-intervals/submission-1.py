class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        
        sorted_intervals = sorted(intervals)
        merged_intervals = [sorted_intervals[0]]

        for start, end in sorted_intervals:
            merged_end = merged_intervals[-1][1]
            if start <= merged_end:
                merged_intervals[-1][1] = max(merged_end, end)
            else:
                merged_intervals.append([start, end]) 
        return merged_intervals


        