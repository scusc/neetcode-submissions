from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        countOfCards = Counter(hand)
        hand.sort()

        for num in hand:
            if countOfCards[num]:
                for i in range(groupSize):
                    if countOfCards[num + i] == 0:
                        return False
                    countOfCards[num + i] -= 1
        return True


        