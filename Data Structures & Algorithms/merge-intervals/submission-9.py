class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals, key=lambda x: x[0])
        output = [intervals[0]]

        for interval in intervals[1:]:
            currStart = interval[0]
            lastEnd = output[-1][1]

            if currStart <= lastEnd:
                output[-1][1] = max(lastEnd, interval[1])

            else:
                output.append(interval)

        return output
        