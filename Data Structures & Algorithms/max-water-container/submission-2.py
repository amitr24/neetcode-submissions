class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_stored = 0

        i = 0
        j = len(heights) - 1

        while (i < j):
            width = (j-i)
            water_stored = (min(heights[i], heights[j]) * width)
            max_stored = max(max_stored, water_stored)
            if(heights[i] < heights[j]):
                #while(heights[i] < heights[j] and i < j):
                i+=1
            else:
                # while(not heights[i] < heights[j] and i < j):
                j-=1
        return max_stored