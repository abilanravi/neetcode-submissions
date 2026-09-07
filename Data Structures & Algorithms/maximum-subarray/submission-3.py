class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        globalBest = currBest = nums[0]

        for num in nums[1:]:
            currBest = max(num, currBest + num)
            globalBest = max(globalBest, currBest)

        return globalBest
        