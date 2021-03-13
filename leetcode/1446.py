class Solution:
    def maxPower(self, s: str) -> int:
        max_len = 0
        temp_len = 1
        a = s[0]

        if len(s) == 1:
            return 1

        else:
            for i in range(1, len(s)):
                if s[i] == a:
                    temp_len += 1

                else:
                    a = s[i]
                    max_len = max(max_len, temp_len)
                    temp_len = 1

            max_len = max(max_len, temp_len)
            return max_len