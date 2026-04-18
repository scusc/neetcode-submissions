class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backTrack(col):
            nonlocal res
            if col == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return 
            
            for row in range(n):
                if row in occupiedRows or (row - col) in occupiedDiag1 or (row + col) in occupiedDiag2:
                    continue
                
                occupiedRows.add(row)
                occupiedDiag1.add(row - col)
                occupiedDiag2.add(row + col)
                board[row][col] = "Q"
                backTrack(col + 1)

                occupiedRows.remove(row)
                occupiedDiag1.remove(row - col)
                occupiedDiag2.remove(row + col)
                board[row][col] = "."

        
        board = [["."] * n for i in range(n)]
        res = []
        occupiedRows, occupiedCols, occupiedDiag1, occupiedDiag2 = set(), set(), set(), set()
        backTrack(0)
        return res
        