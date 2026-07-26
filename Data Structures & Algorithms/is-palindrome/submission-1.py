class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0,len(s)-1
        while l<r:
            if s[l].lower() == s[r].lower():
                l = l+1
                r = r-1
                continue
            elif not(str.isalnum(s[l])):
                l+=1
            elif not(str.isalnum(s[r])):
                r-=1
            else:
                return False
        return True
                
        