class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # true is value appears > 1 
        # false otherwise (1 =< )
        # use hashmap to store the values
        seen = {}
        for num in nums:
            if num in seen:
                return True 
            seen[num]= 1
        return False