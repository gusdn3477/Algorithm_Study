class Solution:
    def isMonotonic(self, A: List[int]) -> bool:

        flag = 1
        flag2 = 1

        if len(A) == 1:
            return True

        else:

            for i in range(1, len(A)):
                if A[i - 1] <= A[i]:
                    flag += 1

                else:
                    flag = 1

            for i in range(1, len(A)):
                if A[i - 1] >= A[i]:
                    flag2 += 1

                else:
                    flag2 = 1

            flag = max(flag, flag2)

            if flag == len(A):
                return True

            else:
                return False