class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}

        for index, char in enumerate(s):
            lastIndex[char] = index
        
        size = end = 0
        res = []

        for index, char in enumerate(s):
            size += 1
            end = max(end, lastIndex[char])

            if end == index:
                res.append(size)
                size = 0
        return res
