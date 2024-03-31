class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minIdx = maxIdx = badIdx = -1
        cnt = 0
        
        for i in range(0, len(nums)):
            if nums[i] == minK:
                minIdx = i
            
            if nums[i] == maxK:
                maxIdx = i
                
            if nums[i] < minK or nums[i] > maxK:
                badIdx = i
            
            cnt += max(0, min(minIdx, maxIdx) - badIdx)
        
        return cnt
                
        
        