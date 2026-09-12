class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x: x[0])
        output = [intervals[0]]

        for interval in intervals[1:]:
            currEnd = output[-1][1]
            newStart = interval[0]

            if currEnd >= newStart:
                output[-1][1] = max(currEnd, interval[1])

            else:
                output.append(interval)

        return output
