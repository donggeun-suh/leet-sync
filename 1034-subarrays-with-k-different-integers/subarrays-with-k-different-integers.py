class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.good_subarray(nums, k) - self.good_subarray(nums, k-1)
        
    def good_subarray(self, nums: List[int], k: int) -> int:
        freq_map = defaultdict(int)
        l = 0
        ans = 0
        
        for r in range(0,len(nums)):
            freq_map[nums[r]] +=1
            
            if len(freq_map) > k:
                while len(freq_map) > k:                    
                    freq_map[nums[l]] -= 1
                    
                    if freq_map[nums[l]] == 0:
                        del freq_map[nums[l]]

                    l +=1
            
            ans += r - l + 1
        
        return ans
                