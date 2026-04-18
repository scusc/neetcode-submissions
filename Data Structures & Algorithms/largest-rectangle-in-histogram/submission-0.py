class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        n = len(heights)

        for i in range(n + 1):
            currentHeight = heights[i] if i < n else -1

            while stack and heights[stack[-1]] >= currentHeight:
                h = heights[stack.pop()]
                widht = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, widht * h)
            
            stack.append(i)
        
        return maxArea
