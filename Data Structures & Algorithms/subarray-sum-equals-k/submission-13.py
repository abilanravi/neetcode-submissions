class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        freq = {0 : 1}
        prefix, res = 0, 0

        for num in nums:
            prefix += num
            want = prefix - k

            res += freq.get(want, 0)
            freq[prefix] = freq.get(prefix, 0) + 1

        return res


            
        