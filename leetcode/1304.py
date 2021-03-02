class Solution:
    def sumZero(self, n: int) -> List[int]:

        arr = []

        if n % 2 == 0:  # 짝수인 경우

            for i in range(1, n // 2 + 1):
                arr.append(i)

            for i in range(-(n // 2), 0):
                arr.append(i)

        else:  # 홀수인 경우

            for i in range(1, n // 2 + 1):
                arr.append(i)

            for i in range(-(n // 2), 0):
                arr.append(i)

            arr.append(0)

        return arr