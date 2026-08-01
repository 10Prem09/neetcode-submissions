class Solution:
    def isValid(self, s: str) -> bool:
        sStack = []
        if len(s)%2 !=0:
            return False
        for i in range(len(s)):
            if s[i] in ['(', '{', '[']:
                sStack.append(s[i])
            else:
                if not(sStack):
                    return False 
                top = sStack[-1]
                if (top, s[i]) not in [('(',')'), ('{','}'), ('[',']')]:
                    return False
                sStack.pop()
        if sStack:
            return False
        return True