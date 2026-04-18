class Trie:
    def __init__(self):
        self.root = {}
        self.end = "*"
    
    def insert(self, word):
        curnode = self.root
        for char in word:
            if char not in curnode:
                curnode[char] = {}
            curnode = curnode[char]
        curnode[self.end] = word


class Solution:

    def getNeighbors(self, row, col, board):
        neighbors = []
        direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in direction:
            nx, ny = row + dx, col + dy
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                neighbors.append([nx, ny])
        
        return neighbors


    def explore(self, row, col, board, node, visited, finalwords):
        if visited[row][col] or board[row][col] not in node:
            return
        
        visited[row][col] = True
        node = node[board[row][col]]

        if "*" in node:
            finalwords.add(node["*"])
        
        neighbors = self.getNeighbors(row, col, board)

        for nei in neighbors:
            self.explore(nei[0], nei[1], board, node, visited, finalwords)
        
        visited[row][col] = False


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        visited = [[False for _ in row] for row in board]
        finalwords = set()

        for word in words:
            trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.explore(i, j, board, trie.root, visited, finalwords)
        
        return list(finalwords)