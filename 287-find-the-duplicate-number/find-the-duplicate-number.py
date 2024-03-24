class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        _dict = dict()
        
        for num in nums:
            if num in _dict:
                return num
            else:
                _dict[num] = 1
        