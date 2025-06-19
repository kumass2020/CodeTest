class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        new_start, new_end = newInterval
        n = len(intervals)
        i = 0

        answer = []
        while i < n and intervals[i][1] < new_start:
            answer.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        
        answer.append([new_start, new_end])

        while i < n:
            answer.append(intervals[i])
            i += 1
        
        return answer


        # if not intervals:
        #     return [newInterval]

        # new_start, new_end = newInterval

        # answer = []
        # real_start = real_end = None
        # inserted = False
        # eps = 0.0001
        
        # for i, interval in enumerate(intervals):
        #     start, end = interval

        #     if start <= new_start <= new_end <= end:
        #         answer.append(interval)
        #         inserted = True
        #         continue
        #     if new_start <= start <= end <= new_end:
        #         if i == len(intervals)-1:
        #             answer.append(newInterval)
        #             break
        #         if not real_start:
        #             real_start = new_start
        #             if real_start == 0:
        #                 real_start += eps
        #             continue

        #     if not inserted:
        #         if not real_start:
        #             if new_end < start:
        #                 answer.append([new_start, new_end])
        #                 inserted = True
        #             if end < new_start and i == len(intervals)-1:
        #                 answer.append(interval)
        #                 answer.append([new_start, new_end])
        #                 break
        #             if i == len(intervals)-1 and (start <= new_start <= end or start <= new_end <= end):
        #                 answer.append([min(start, new_start), max(end, new_end)])
        #                 break
                        
        #         else:
        #             if new_end == end:
        #                 answer.append([int(real_start), new_end])
        #                 inserted = True
                    
        #             elif start <= new_end <= end:
        #                 answer.append([int(real_start), end])
        #                 inserted = True
        #                 continue
                        
        #             elif new_end < start:
        #                 answer.append([int(real_start), new_end])
        #                 inserted = True
                        
        #             elif new_end == start:
        #                 answer.append([int(real_start), end])
        #                 inserted = True
        #                 continue

        #             elif i == len(intervals)-1:
        #                 answer.append([int(real_start), max(new_end, end)])
        #                 break

        #     if not real_start and not inserted and new_start <= end:
        #         real_start = min(start, new_start)

        #         if real_start == 0:
        #             real_start += eps

        #         if i == len(intervals)-1:
        #             answer.append([min(start, new_start), max(end, new_end)])

        #         continue

        #         # if end >= new_start:
        #         #     real_end = new_end

        #     # elif start <= new_end <= end:
        #     #     real_end = end
        #     if inserted or not real_start:
        #         answer.append(interval)
            
        #     # if real_start and real_end:
        #     #     answer.append([real_start, real_end])
        #     #     real_start = real_end = None

        # return answer
