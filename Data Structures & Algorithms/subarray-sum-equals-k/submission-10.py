class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        prefix, count = 0, 0

        freq = { 0 : 1}

        for num in nums:
            prefix += num
            want = prefix - k

            count += freq.get(want, 0)
            freq[prefix] = 1 + freq.get(prefix, 0)

        return count
