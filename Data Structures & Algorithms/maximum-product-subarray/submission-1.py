class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        currMax = currMin = totalMax = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            newMin = min(currMin * num, num, currMax * num)
            newMax = max(currMax * num, currMin * num, num)
            currMax = newMax
            currMin = newMin
            totalMax = max(totalMax, newMax)

        return totalMax