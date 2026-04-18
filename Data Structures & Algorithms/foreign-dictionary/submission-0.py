class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {char: set() for word in words for char in word}
        indegrees = {char: 0 for char in adj}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            minLen = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:minLen] == word2:
                return ""

            for j in range(minLen):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        indegrees[word2[j]] += 1
                    break
        q = deque([char for char in indegrees if indegrees[char] == 0])
        res = []

        while q:
            char = q.popleft()
            res.append(char)
            for neighbor in adj[char]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        
        if len(res) != len(indegrees):
            return ""
        return "".join(res)
        