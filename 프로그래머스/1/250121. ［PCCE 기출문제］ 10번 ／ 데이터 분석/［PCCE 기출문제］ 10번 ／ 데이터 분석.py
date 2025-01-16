def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    data_map = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}
    new_data = []
    
    for d in data:
        if d[data_map[ext]] < val_ext:
            new_data.append(d)
    
    sorted_data = sorted(new_data, key=lambda x: x[data_map[sort_by]])
    
    return sorted_data