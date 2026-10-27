class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        
        sorted_intervals = sorted(intervals) #Intervals is now sorted in asc order based on intervals
        merged_array = [sorted_intervals[0]] #Merge_array = [[1,3]]

        for start, end in sorted_intervals[1:]: #[[1, 5], [6,7]]
            merge_end = merged_array[-1][1] # End of the merged array 3

            if start <= merge_end: # 5 <= 6
                merged_array[-1][1] = max(merge_end, end) #Max between 
            else:
                merged_array.append([start, end])
        return merged_array

        