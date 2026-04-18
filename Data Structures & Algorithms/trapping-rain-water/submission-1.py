class Solution:
    def trap(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0

        left = 0
        right = len(heights) - 1

        leftMax = heights[left]
        rightMax = heights[right]

        area = 0

        while left < right:
            if heights[left] < heights[right]:
                left += 1
                leftMax = max(leftMax, heights[left])
                area += leftMax - heights[left]

            else:
                right -= 1
                rightMax = max(rightMax, heights[right])
                area += rightMax - heights[right]
        
        return area
        