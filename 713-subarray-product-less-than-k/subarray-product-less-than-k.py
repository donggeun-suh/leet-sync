class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        
        
        _cnt = 0
        s = 1
        j = 0
        
        for i in range(0,len(nums)):
            s *= nums[i]
            
            while s >= k and j <= i:
                s /= nums[j]
                j += 1
            
            if j > i:
                continue
            
            _cnt += i-j + 1
                    
        return _cnt