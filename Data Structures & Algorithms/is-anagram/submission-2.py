class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            s_letter_count = s_dict.get(s[i], 0)
            s_dict[s[i]] = s_letter_count + 1

            t_letter_count = t_dict.get(t[i], 0)
            t_dict[t[i]] = t_letter_count + 1 

        print(s_dict, t_dict)
    
        for key, value in s_dict.items():
            if t_dict.get(key, None) != value:
                return False
        
        return True
