class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for num, value in enumerate(nums):
            complement = target - value
            
            if complement in seen:
                return [seen[complement], num]
            
            seen[value] = num
            
        