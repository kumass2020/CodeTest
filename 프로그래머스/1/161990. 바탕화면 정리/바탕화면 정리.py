def solution(wallpaper):
    answer = []
        
    x_coord_min = 50
    x_coord_max = 0
    y_coord_min = 50
    y_coord_max = 0
        
    for i, row in enumerate(wallpaper):
        # x_coords = row.find('#')
        x_coords = [i for i, x_coord in enumerate(row) if x_coord == '#']
        y_coord = i
        
        if x_coords != -1:
            if isinstance(x_coords, int):
                x_coord = x_coords
                if x_coord < x_coord_min:
                    x_coord_min = x_coord
                if x_coord > x_coord_max:
                    x_coord_max = x_coord

                if y_coord < y_coord_min:
                    y_coord_min = y_coord
                if y_coord > y_coord_max:
                    y_coord_max = y_coord
            else:
                for x_coord in x_coords:
                    if x_coord < x_coord_min:
                        x_coord_min = x_coord
                    if x_coord > x_coord_max:
                        x_coord_max = x_coord

                    if y_coord < y_coord_min:
                        y_coord_min = y_coord
                    if y_coord > y_coord_max:
                        y_coord_max = y_coord

        
    x_coord_max += 1
    y_coord_max += 1
        
    answer = [y_coord_min, x_coord_min, y_coord_max, x_coord_max]
    
    return answer