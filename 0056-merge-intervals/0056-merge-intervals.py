class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        # intervals.sort(key=lambda x: (x[0], x[1]))
        intervals.sort(key=lambda x: x[0])

        # print(intervals)
        answer = []
        for i, intv in enumerate(intervals):
            if i == 0:
                answer.append(intv)
                continue

            if i > 0:
                prev = answer[-1]
                # print(intervals[i-1], intv)
                if intv[1] <= intervals[i-1][1]:
                    continue

                if intv[0] <= prev[1]:
                    # print(min(answer[-1][0], intv[0]))
                    # start = min(answer[-1][0], intv[0])
                    start = prev[0]
                    end = max(prev[1], intv[1])
                    answer[-1] = [start, end]
                else:
                    answer.append(intv)

        return answer
