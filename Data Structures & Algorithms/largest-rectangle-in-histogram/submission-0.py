class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        max_area = 0
        stack = [] #only the indices?
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                area = height*width
                max_area = max(area, max_area)
            stack.append(i)
        return max_area
                
            