class Solution:

    def nextNum(self, n):
        total = 0
        while n > 0:
            digit = n % 10       # get last digit
            total += digit * digit
            n //= 10            # remove last digit to get next last digit
        return total

    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)
            n = self.nextNum(n)
        
        return True
