class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        finalArea = 0
        
        while left < right:
            height = min(heights[left], heights[right])
            width = right - left
            finalArea = max(finalArea, height*width)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return finalArea