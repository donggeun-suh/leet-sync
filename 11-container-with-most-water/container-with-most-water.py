class Solution:
    def maxArea(self, height: List[int]) -> int:
        mem = 0
        r = len(height) -1
        l = 0
        
        while l < r :
            mem = max(mem, (r-l) * min(height[r], height[l]))
            
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        
        return mem
            