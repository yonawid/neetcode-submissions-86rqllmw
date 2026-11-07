class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r=0,len(heights)-1
        area=0
        while l < r:
            if heights[l] > heights[r]:
                area=max(heights[r]*(r-l),area)
                r-=1
            else:
                area=max(heights[l]*(r-l),area)
                l+=1
    
        return area