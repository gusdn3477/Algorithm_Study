class Solution:
    def reverseWords(self, s: str) -> str:

        answer = ''
        st = ''

        for i in range(len(s)):
            if s[i] == ' ':
                answer += st[::-1]
                answer += ' '
                st = ''

            else:
                st += s[i]

        if st:
            answer += st[::-1]

        return answer