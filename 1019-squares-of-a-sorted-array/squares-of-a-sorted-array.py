class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared_list = [ num**2  for num in nums]
        return sorted(squared_list, reverse=False)