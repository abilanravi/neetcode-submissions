class Solution:
    def rob(self, nums: List[int]) -> int:

        first, second = 0, 0

        for num in nums:
            temp = max(second, num+first)
            first = second
            second = temp

        return second
