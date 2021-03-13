class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        dic = {}

        for i in nums:

            if i not in dic.keys():
                dic[i] = 1

            else:
                dic[i] += 1

        dic_sort = sorted(dic.values())

        if dic_sort[-1] >= 2:
            return True

        else:
            return False