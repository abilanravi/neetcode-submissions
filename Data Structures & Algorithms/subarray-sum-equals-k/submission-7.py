class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        count = 0
        freq = {0:1}

        for num in nums:
            prefix += num
            sol = prefix - k

            if sol in freq:
                count += freq[sol]
            freq[prefix] = freq.get(prefix, 0) + 1

        return count