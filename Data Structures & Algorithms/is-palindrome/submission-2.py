class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Approach: Two-Pointer (bc need begining & end tracking & is sorted)
        # Types: string s
        # Returns: true if palindrome
        # Logic: must be case sensitive 

        left = 0  # begining
        right = len(s)-1 # end

        while left < right:
            # accounting for the non numeric properies of the string
            while left < right and not s[left].isalnum():
                left += 1  # stops as soon as left reaches right

            while left < right and not s[right].isalnum():
                right -= 1  # stops as soon as right reaches left

            if s[left].lower() != s[right].lower(): # check if palindrome or not is case sensitive
                return False
            
            left +=1
            right -=1
        return True
