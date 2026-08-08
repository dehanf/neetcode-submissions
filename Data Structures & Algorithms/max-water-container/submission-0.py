class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_vol = 0 
        temp_vol =0

        while left < right:
            
            
            if heights[left] > heights[right]:
                temp_vol = (right-left)*heights[right]
                right -= 1
            else: 
                temp_vol = (right-left)*heights[left]
                left += 1
            if max_vol < temp_vol:
                max_vol = temp_vol 
        return max_vol





