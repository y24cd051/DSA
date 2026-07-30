class Solution:
    def maxArea(self, heights: List[int]) -> int:
        area=0
        max_area=0
        i=0
        j=len(heights)-1
        while i<j:
            length=j-i
            breadth=min(heights[i],heights[j])
            area=length*breadth
            max_area=max(max_area,area)
            if heights[j]>=heights[i]:
                i+=1
            else:
                j-=1
        return max_area

        