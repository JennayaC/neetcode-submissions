class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        result = 0
        mySet = set(nums)

        for num in mySet:
            if num - 1 not in mySet:
                length = 1

                while num + length in mySet:
                    length += 1
                result = max(result, length)

        return result
            
            
        
      