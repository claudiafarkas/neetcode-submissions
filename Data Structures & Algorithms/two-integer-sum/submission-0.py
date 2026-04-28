class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # array; nums 
        # int target
        # hashmap problem

        seen = {}   # define seen dict for numbers already visited

        for i, num in enumerate(nums):  # since need to keep track of index and number
            complement = target - num      # check the difference
            if complement in seen:      # check if number in seen dict
                return [seen[complement], i]       # if in seen then return the number and its compliement
            seen[num] = i       # update seen with visited number 