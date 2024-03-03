class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        _len = len(s)
        _count = 0
        ans = ""
        
        for num in s:
            if num == "1":
                _count += 1
                
        _count -= 1
        
        for i in range(0, _len -1):
            if _count > 0:
                _count -= 1
                ans += "1"
            else:
                ans += "0"
                
        return ans + "1"