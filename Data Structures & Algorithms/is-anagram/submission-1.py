class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s=list(s)
        sorted_t=list(t)
        sorted_s.sort()
        sorted_t.sort()
        if len(sorted_s)!=len(sorted_t):
            return False
        else:
            for i in range(len(sorted_s)):
                if (sorted_s[i]!=sorted_t[i]):
                    return False
            return True