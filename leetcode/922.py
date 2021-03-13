class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        arr = [i for i in nums if i % 2 == 0]
        arr2 = [i for i in nums if i % 2 == 1]
        arr3 = []

        for i in range(len(arr)):
            arr3.append(arr[i])
            arr3.append(arr2[i])

        return arr3