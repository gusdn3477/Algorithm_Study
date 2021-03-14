class Solution:
    def isPowerOfFour(self, n: int) -> bool:

        x = 1

        for i in range(32):

            if x == n:
                return True

            x *= 4

        return False