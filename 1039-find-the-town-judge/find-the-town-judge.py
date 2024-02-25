class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0] * (n + 1)
        trusting = [0] * (n + 1)
        
        for t in trust:
            trusting[t[0]] += 1
            trusted[t[1]] += 1
        
        ans = -1
        
        for i in range(1, n+1):
            if trusted[i] == n-1 and trusting[i] == 0:
                ans = i
                
        
        return ans