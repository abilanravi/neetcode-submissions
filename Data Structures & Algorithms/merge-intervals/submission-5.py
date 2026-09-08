class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]

        for interval in intervals[1:]:
            currEnd = res[-1][1]
            nextStart = interval[0]

            if nextStart <= currEnd:
                res[-1][1] = max(currEnd, interval[1])

            else:
                res.append(interval)
        
        return res  