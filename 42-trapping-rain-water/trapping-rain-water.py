class Solution:
    def trap(self, height: List[int]) -> int:
        l = len(height)
        left = [0] * l
        right = [0] * l
        ans = 0 
        
        left[0] = height[0]
        for i in range(1, l):
            left[i] = max(left[i - 1], height[i])
        
        right[l-1] = height[l-1]
        for i in range(l-2, -1, -1):
            right[i] = max(right[i + 1], height[i])
            
        
        for i in range(0, l):
            ans += min(left[i], right[i]) - height[i]
            
        
        return ans
            
        
        
            

                
            