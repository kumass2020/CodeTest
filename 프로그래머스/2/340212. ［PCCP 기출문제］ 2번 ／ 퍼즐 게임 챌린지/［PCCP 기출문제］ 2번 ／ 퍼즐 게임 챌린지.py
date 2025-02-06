def solution(diffs, times, limit):
    
#     time_accum = 10**15
#     level_start = 1
    
#     while time_accum > limit:
#         time_accum = 0
#         level = level_start
        
#         for i, (diff, time) in enumerate(zip(diffs, times)):
#             if diff <= level:
#                 time_accum += time
#             else:
#                 time_accum += (diff - level) * (time + times[i-1]) + time
                
#             if time_accum > limit:
#                 break
        
#         level_start *= 2
        
    
#     for level in range(int(level_start/4), limit+1):
#         time_accum = 0
        
#         for i, (diff, time) in enumerate(zip(diffs, times)):
#             if diff <= level:
#                 time_accum += time
#             else:
#                 time_accum += (diff - level) * (time + times[i-1]) + time
                
#             if time_accum > limit:
#                 break
            
#         if time_accum <= limit:
#             return level   

#     level = int(limit / 2)
#     search_space = int(level / 2)
#     while True:
#         time_accum = 0
        
#         for i, (diff, time) in enumerate(zip(diffs, times)):
#             if diff <= level:
#                 time_accum += time
#             else:
#                 time_accum += (diff - level) * (time + times[i-1]) + time
                
#             if time_accum > limit:
#                 level = level + search_space
#                 break
            
#         if time_accum <= limit:
#             if search_space == 1:
#                 return level
#             level = level - search_space
        
#         search_space = int(search_space / 2)
        
    n = len(diffs)
    
    # Function to calculate total time given a level.
    def total_time(level):
        total = times[0]  # Puzzle 0 is always solved correctly (since diffs[0] == 1 and level>=1)
        for i in range(1, n):
            # If the puzzle's difficulty is within your level, no mistakes are made.
            if diffs[i] <= level:
                total += times[i]
            else:
                # Number of mistakes
                mistakes = diffs[i] - level
                # Each mistake costs: current puzzle time + previous puzzle time.
                # After making mistakes, you finally solve the puzzle (cost = current puzzle time).
                total += mistakes * (times[i] + times[i-1]) + times[i]
            # Early exit if the total time already exceeds the limit.
            if total > limit:
                return total
        return total

    # The maximum possible level you need to consider is max(diffs) because if level >= max(diffs),
    # then you never make any mistakes and the total time is simply sum(times).
    low, high = 1, max(diffs)
    answer = high  # Initialize answer to the highest possible value.

    while low <= high:
        mid = (low + high) // 2
        if total_time(mid) <= limit:
            answer = mid  # mid is a candidate; try to see if you can lower the level further.
            high = mid - 1
        else:
            low = mid + 1

    return answer
        
        