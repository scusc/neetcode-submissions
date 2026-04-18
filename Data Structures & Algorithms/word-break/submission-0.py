from typing import List

class Trie:
    def __init__(self):
        self.root = {}

    def insert_word(self, word: str) -> None:
        current = self.root
        for char in word:
            if char not in current:
                current[char] = {}
            current = current[char]
        current['*'] = True

    def is_word_in_range(self, text: str, start: int, end: int) -> bool:
        current = self.root
        for index in range(start, end + 1):
            if text[index] not in current:
                return False
            current = current[text[index]]
        return '*' in current


class Solution:
    def wordBreak(self, text: str, wordDict: List[str]) -> bool:
        trie = Trie()
        for word in wordDict:
            trie.insert_word(word)

        n = len(text)
        can_break_from = [False] * (n + 1)
        can_break_from[n] = True

        max_word_length = max(len(word) for word in wordDict)

        for start in range(n - 1, -1, -1):
            for end in range(start, min(n, start + max_word_length)):
                if trie.is_word_in_range(text, start, end):
                    if can_break_from[end + 1]:
                        can_break_from[start] = True
                        break

        return can_break_from[0]