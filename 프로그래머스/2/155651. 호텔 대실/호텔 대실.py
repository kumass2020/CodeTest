def solution(book_time):
    room = 0
    
    book_time_min = []
    
    for start, end in book_time:
        start_min = int(start[:2]) * 60 + int(start[3:])
        end_min = int(end[:2]) * 60 + int(end[3:]) + 10
        
        book_time_min.append([start_min, end_min])
    
    # start time을 기준으로 정렬
    book_time_min.sort(key=lambda x: x[0])
    
    room_dict = {}
    
    # start time이 빠른 것부터 방 배정
    for i, (start, end) in enumerate(book_time_min):
        if i == 0:
            room += 1
            room_dict[0] = end
        else:
            counter = 0
            for j in range(0, len(room_dict)):
                if room_dict[j] <= start:
                    room_dict[j] = end
                    counter += 1
                    break
            
            if not counter:
                room += 1
                room_dict[len(room_dict)] = end
                
            
    
    return room