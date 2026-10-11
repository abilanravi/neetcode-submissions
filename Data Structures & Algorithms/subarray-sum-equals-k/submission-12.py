class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        count = {0 : 1}
        currentSum = 0
        result = 0

        for num in nums:
            currentSum += num
            want = currentSum - k

            result += count.get(want, 0)
            count[currentSum] = 1 + count.get(currentSum, 0)

        return result


            
        