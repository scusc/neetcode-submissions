from collections import Counter, defaultdict

class Solution:
    def minWindow(self, big: str, small: str) -> str:
        targetCount = Counter(small)
        windowCount = defaultdict(int)

        res, resLen = [-1, -1], float('inf')
        have = 0
        left = 0

        for right in range(len(big)):
            char = big[right]
            windowCount[char] += 1

            if char in targetCount and targetCount[char] == windowCount[char]:
                have += 1

            
            while have == len(targetCount):
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                leftChar = big[left]
                windowCount[leftChar] -= 1

                if leftChar in targetCount and windowCount[leftChar] < targetCount[leftChar]:
                    have -= 1
                
                left += 1
        
        return big[res[0] : res[1] + 1] if resLen != float('inf') else ""