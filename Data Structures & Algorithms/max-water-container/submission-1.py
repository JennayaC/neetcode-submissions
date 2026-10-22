class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            area = min(heights[left],heights[right]) * (right - left)
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
            max_water = max(area, max_water)
        return max_water

        