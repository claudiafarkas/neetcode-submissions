class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     # Approach: Hashmap (since keeping track of value and position)
     # Types: array of int nums, int target
     # Arithmetic: complement = target - num[i]
     # return complement[i], num[i]

     seen = {}  # dict for hashmap
     for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i   # stored the seen number seen[3] 

