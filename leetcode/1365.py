class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        answer = []

        for i in range(len(nums)):
            total = 0
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    total += 1

            answer.append(total)

        return answer