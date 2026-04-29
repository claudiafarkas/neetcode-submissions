class Solution:
    def isHappy(self, n: int) -> bool:
     # non-cyclical: positive number, 
     # keep track of position and vale
     # slpit up the number into digits then square and add each digit
     # hashmap 

        if n < 0:
            return False
        
        seen = set()
        while n not in seen:
            seen.add(n)
            n = self.sum_of_squares(n)
        return n == 1

    def sum_of_squares(self, n):
        total = 0
        for d in str(n):        # convert to string to deperate digits
            total+= int(d) ** 2     # then ^2 foe each integer digits
        return total    

    
   





