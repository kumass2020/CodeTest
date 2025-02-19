# class Robot():
#     def move(start, end):
#         c_pos = start
#         trajectory = []
#         # trajectory.append(c_pos)
        
#         while c_pos != end:
#             trajectory.append(tuple(c_pos))
#             if c_pos[0] > end[0]:
#                 c_pos[0] -= 1
#             elif c_pos[0] < end[0]:
#                 c_pos[0] += 1
#             elif c_pos[1] > end[1]:
#                 c_pos[1] -= 1
#             elif c_pos[1] < end[1]:
#                 c_pos[1] += 1
            
#         return trajectory
            

# def solution(points, routes):
#     answer = 0
#     trajectories = []
    
#     for i in range(len(routes)):
#         for j in range(len(routes[i])-1):
#             start_idx = routes[i][j]-1
#             end_idx = routes[i][j+1]-1

#             start = points[start_idx]
#             end = points[end_idx]
            
#             if j == 0:
#                 trajectories.append(Robot.move(start, end))
#             else:
#                 trajectories[i].extend(Robot.move(start, end))
    
#     for i in range(max(len(trajectory) for trajectory in trajectories)):
#         current_pos = []
#         for j in range(len(trajectories)):
#             if i < len(trajectories[j]):
#                 current_pos.append(trajectories[j][i])
        
#         if len(current_pos) != len(set(current_pos)):
#             answer += len(current_pos) - len(set(current_pos))
            
    
#     return answer

def solution(points, routes):
    def move_path(start, end):
        path = []
        cur_r, cur_c = start
        
        path.append((cur_r, cur_c))
        
        while (cur_r, cur_c) != end:
            if cur_r != end[0]:
                if cur_r < end[0]:
                    cur_r += 1
                else:
                    cur_r -= 1
            else:
                if cur_c < end[1]:
                    cur_c += 1
                else:
                    cur_c -= 1
            path.append((cur_r, cur_c))
        return path
    
    trajectories = []
    for route in routes:
        traj = []
        for i in range(len(route) - 1):
            start_idx = route[i] - 1
            end_idx = route[i+1] - 1
            start = tuple(points[start_idx])
            end = tuple(points[end_idx])
            segment = move_path(start, end)
            if i > 0:
                segment = segment[1:]
            traj.extend(segment)
        trajectories.append(traj)
    
    max_time = max(len(traj) for traj in trajectories)
    risk_count = 0
    
    for t in range(max_time):
        pos_occurrences = {}
        for traj in trajectories:
            if t < len(traj):
                pos = traj[t]
                pos_occurrences[pos] = pos_occurrences.get(pos, 0) + 1
        
        for count in pos_occurrences.values():
            if count >= 2:
                risk_count += 1
    
    return risk_count
