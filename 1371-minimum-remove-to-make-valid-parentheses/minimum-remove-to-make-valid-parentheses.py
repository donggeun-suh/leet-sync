class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        s = list(s)
        
        for i in range (0, len(s)):
            if s[i] == '(':
                stack.append(i)
                
            if s[i] == ')':
                if not stack:
                    s[i] = ' '
                else:
                    stack.pop()
            
        if stack:
            for m in stack:
                s[m] = ' '
        
        return ''.join(s).replace(' ', '')