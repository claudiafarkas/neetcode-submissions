class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      # int array; nums
      # return true if value appears more than 1
      # else false

      #pseudo code
      # goal iterate through the array to find if any values appear more then once, 
      # assumtion: as soon as there is a duplicate return true

        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False