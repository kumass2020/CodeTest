def solution(video_len, pos, op_start, op_end, commands):
    video_len_sec = int(video_len[:2]) * 60 + int(video_len[3:])
    pos_sec = int(pos[:2]) * 60 + int(pos[3:])
    op_start_sec = int(op_start[:2]) * 60 + int(op_start[3:])
    op_end_sec = int(op_end[:2]) * 60 + int(op_end[3:])
        
    for command in commands:
        if op_start_sec <= pos_sec <= op_end_sec:
            pos_sec = op_end_sec
        
        if command == "next":
            pos_sec += 10
        elif command == "prev":
            pos_sec -= 10
        
        if pos_sec < 0:
            pos_sec = 0
        if pos_sec > video_len_sec:
            pos_sec = video_len_sec
        
    if op_start_sec <= pos_sec <= op_end_sec:
        pos_sec = op_end_sec
    
    pos = f"{str(int(pos_sec / 60)).zfill(2)}:{str(pos_sec % 60).zfill(2)}"
    answer = pos
    return answer