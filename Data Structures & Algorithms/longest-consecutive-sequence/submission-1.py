class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        seen = set(nums)
        longest = 0

        for num in seen:
            # Only start counting if this is the beginning of a sequence
            if num - 1 not in seen:
                current = num
                length = 1

                # Count the consecutive numbers after it
                while current + 1 in seen:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest