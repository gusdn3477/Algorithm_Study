class Solution:
    def totalMoney(self, n: int) -> int:

        ct = 0
        total = 0
        flag = -1
        day = 1

        for i in range(0, n):

            if i % 7 == 0:
                flag += 1
                day = 1

            total += flag + day

            day += 1

        return total