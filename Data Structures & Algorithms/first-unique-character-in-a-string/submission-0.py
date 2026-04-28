class Solution:
    def firstUniqChar(self, s: str) -> int:
        # hashmap to keep track

        seen = {}   # define dict for seen letters, has key value for character and occurance
        if len(s) == 0:
            return -1

        for val in s:       # builds the hashmap → only need value → skip enumerate
            seen[val] = seen.get(val, 0) + 1
        
        for i, val in enumerate(s): # searches for answer → need index to return → use enumerate
            if seen[val] == 1:
                return i
        return -1
        


        