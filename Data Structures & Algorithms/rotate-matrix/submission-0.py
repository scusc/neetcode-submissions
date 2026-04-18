class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # to rotate, we need to transpose a matrix and then reverse the rows
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for row in matrix:
            left, right = 0, n - 1 
            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1

