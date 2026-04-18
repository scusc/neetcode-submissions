class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives = tens = 0
        for bill in bills:
            if bill == 5:
                fives += 1
            elif bill == 10:
                fives, tens = fives - 1, tens + 1
            elif tens > 0:
                fives, tens = fives - 1, tens - 1
            else:
                fives -= 3

            if fives < 0:
                return False
        return True