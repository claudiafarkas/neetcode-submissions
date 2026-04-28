class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        # len(s) == len(t)
        for i in range(len(s)):
            s_dict[s[i]] = 0
            t_dict[t[i]] = 0

 #       {"r": 0, "a": 0, "c": 0, ...}

        for i in range(len(s)):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

#       {"r": 2, "a": 2, "c": 2, "e": 1}
        for key, value in s_dict.items():
            if t_dict.get(key, None) != value:
                return False
        
        return True
