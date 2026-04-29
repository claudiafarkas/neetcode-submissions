class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Approach: Hashmap (keeping track of value and index)
        # Types: two strings, s and t
        # Returns: true if the two string are anagrams of eachother
        # Logic: contains exact same characters; first check if string are same length

        seen_s = {}
        seen_t = {}

        if len(s) != len(t):    # same length check
            return False

        for i, c in enumerate(s):     # only care about index not value for s
            seen_s[c] = seen_s.get(c, 0)+1

        for i, c in enumerate(t):
            seen_t[c] = seen_t.get(c, 0)+1
        
        if seen_s == seen_t:
            return True
        return False

            
