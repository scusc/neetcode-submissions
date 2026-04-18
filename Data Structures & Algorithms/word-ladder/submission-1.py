from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        graph = defaultdict(list)

        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                graph[pattern].append(word)
        
        visited = set([beginWord])
        q = deque([(beginWord, 1)])
    
        while q:
            word, level = q.popleft()
            if word == endWord:
                return level
            
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                for neiWord in graph[pattern]:
                    if neiWord not in visited:
                        visited.add(neiWord)
                        q.append((neiWord, level + 1))
        return 0