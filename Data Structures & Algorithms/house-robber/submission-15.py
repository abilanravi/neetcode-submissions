class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        one, two = nums[0], max(nums[0], nums[1])
        tmp = max(one, two)


        for i in range(2, len(nums)):
            tmp = max(nums[i] + one, two)
            one = two
            two = tmp

        return tmp

        