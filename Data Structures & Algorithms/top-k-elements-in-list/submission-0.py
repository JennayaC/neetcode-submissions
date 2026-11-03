import heapq
"""
Inputs:
1. An array of Integers
2. k, which is an integer

return:
1. An array of the most seen integers in the array

variables:
1. most_seen = []: The most seen integers of the array
2. nums = [...]:The array of integers
3. seen = {}: A dictionary/hashmap that keeps track of how many times we have seen a number in nums

egde cases:
1. If k is greater than len(nums)
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        buckets = [[] for i in range(len(nums) + 1)]
        seen = {}
        result = []

        #Edge case
        if k > len(nums):
            print("Error: k cannot be greater than the length of nums")

        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        for num, count in seen.items():
            buckets[count].append(num)
               
        for i in range(len(buckets)-1,-1,-1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
            
       

        
    