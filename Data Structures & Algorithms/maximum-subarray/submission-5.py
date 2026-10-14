class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        currMax = totalMax = nums[0]

        for num in nums[1:]:
            currMax = max(currMax + num, num)
            totalMax = max(currMax, totalMax)

        return totalMax
        