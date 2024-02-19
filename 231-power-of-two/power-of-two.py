class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1: return True
        if n < 0 or (n % 2 == 1): return False
        
        while n > 1:
            n = n/2
            if n == 1 :
                return True
            
        return False