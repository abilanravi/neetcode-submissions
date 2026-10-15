class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        seen  = {0 : 1}
        count = 0
        prefix = 0

        for num in nums:
            prefix += num
            want = prefix - k
            
            count += seen.get(want, 0)
            seen[prefix] = seen.get(prefix, 0) + 1

        return count
        