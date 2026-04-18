class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows, cols = len(matrix), len(matrix[0])

        firstRowHasZeroes = False
        firstColHasZeroes = False

        for i in range(rows):
            if matrix[i][0] == 0:
                firstColHasZeroes = True
        
        for j in range(cols):
            if matrix[0][j] == 0:
                firstRowHasZeroes = True

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0
        
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0
        
        if firstRowHasZeroes:
            for j in range(cols):
                matrix[0][j] = 0
        
        if firstColHasZeroes:
            for i in range(rows):
                matrix[i][0] = 0