class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        bucketMap = {}

        for word in strs:

            sort = "".join(sorted(word))

            if sort in bucketMap:
                bucketMap[sort].append(word)

            else:
                bucketMap[sort] = [word]

        return list(bucketMap.values())
        