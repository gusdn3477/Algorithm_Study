class Solution:
    def isHappy(self, n: int) -> bool:

        arr = [n]
        total = 0

        while n != 1:

            a = n
            while a > 0:
                total += (a % 10) ** 2
                a //= 10

            if total in arr:
                return False

            arr.append(total)
            n = total
            total = 0

        return True