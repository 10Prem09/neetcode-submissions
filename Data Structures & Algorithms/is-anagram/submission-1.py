class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list_s = list(s)
        list_t = list(t)
        if len(list_s) != len(list_t):
            return False
        for i in list_s:
            if i in list_t:
                list_t.remove(i)
        if list_t == []:
            return True
        return False

        