class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      # Approach: Hashmap (uses set bc only need value)
      # Types: int array; nums
      # Returns: return true if value appears more than 1, else false
      # Logic: goal iterate through the array to find if any values appear more then once, 
      # Assumtions: as soon as there is a duplicate return true

        seen = set()
        for num in nums:   # only value loop
            if num in seen:
                return True
            else:
                seen.add(num)
        return False