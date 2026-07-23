class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        res = 0

        while l < r:

            area = min(heights[l], heights[r]) * (r-l)

            res = max(area, res)


            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return res 
            
#height=[1,7,2,5,4,7,3,6]

        #l             r