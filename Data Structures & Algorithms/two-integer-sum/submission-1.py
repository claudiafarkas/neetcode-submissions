class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     # array of int nums, int target
     # complement = target - num[i]
     # return complement[i], num[i]
     # since keeping track of value and position, using a hashmap approach would be best

     seen = {}  # dict for hashmap

     for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i       # stored the seen number seen[3] and its corresponding index

