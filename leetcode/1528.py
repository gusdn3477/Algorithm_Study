class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        st = ''
        for i in range(len(indices)):
            st += s[indices.index(i)]

        return st