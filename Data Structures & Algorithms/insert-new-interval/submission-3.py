class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for start, end in intervals:
            if end < newInterval[0]:
                res.append([start, end])

            elif start > newInterval[1]:
                res.append([newInterval[0], newInterval[1]])
                newInterval[0], newInterval[1] = start, end

            else:
                newInterval[0], newInterval[1] = min(start, newInterval[0]), max(end, newInterval[1])

        res.append([newInterval[0], newInterval[1]])

        return res
        