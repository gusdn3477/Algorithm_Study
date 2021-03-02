class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        total = 0
        total2 = 0

        for i in range(len(mat)):
            for j in range(len(mat)):
                if i == j:
                    total += mat[i][j]

                if i == len(mat) - j - 1:
                    total2 += mat[i][j]

        if len(mat) % 2 == 0:
            return total + total2

        else:
            return total + total2 - mat[len(mat) // 2][len(mat) // 2]