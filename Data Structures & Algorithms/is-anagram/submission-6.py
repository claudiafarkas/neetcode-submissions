class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # two strings, s and t
        # true if the two string are anagrams of eachother
        # contains exact same characters; first check if strign are same length
        # if len(s) > len(t) or len(s) < len(t):
        #     return False

        seen_s = {}
        seen_t = {}

        if len(s) != len(t):
            return False

        for i, c in enumerate(s):     # only care about index not value for s
            seen_s[c] = seen_s.get(c, 0)+1

        for i, c in enumerate(t):
            seen_t[c] = seen_t.get(c, 0)+1
        
        if seen_s == seen_t:
            return True
        return False

            
