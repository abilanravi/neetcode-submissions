from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        parent = {}
        size = {}

        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a: int, b: int) -> None:
            rootA = find(a)
            rootB = find(b)

            if rootA == rootB:
                return

            if size[rootA] < size[rootB]:
                rootA, rootB = rootB, rootA

            parent[rootB] = rootA
            size[rootA] += size[rootB]

        for num in nums:
            if num not in parent:
                parent[num] = num
                size[num] = 1

        for num in parent:
            if num + 1 in parent:
                union(num, num + 1)

        return max(size[find(num)] for num in parent)