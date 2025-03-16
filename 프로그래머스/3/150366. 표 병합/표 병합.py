# def solution(commands):
#     answer = []
    
#     table = [[''] * 50 for i in range(50)]
#     merge_list = []
    
# #     def init_table(table, r, c):
# #         ex_r = len(table)
# #         ex_c = len(table[0])
        
# #         if ex_r < r:
# #             table.append(['.'] * ex_c) for i in range(r - ex_r)
# #         if ex_c < c:
# #             for i in range(c):
# #                 table[i].append('.')
        
# #         return table
    
#     for command in commands:
#         args_list = command.split(' ')
        
#         if args_list[0] == "UPDATE":
#             if len(args_list) == 4:     # 1.
#                 r = int(args_list[1])-1
#                 c = int(args_list[2])-1
#                 value = args_list[3]
                
#                 table[r][c] = value
                
#                 for cell in merge_list:
#                     if (r, c) in cell:
#                         for curr_r, curr_c in cell:
#                             table[curr_r][curr_c] = value
                    
#             elif len(args_list) == 3:   # 2.
#                 value1 = args_list[1]
#                 value2 = args_list[2]
                
#                 for i in range(50):
#                     for j in range(50):
#                         if table[i][j] == value1:
#                             table[i][j] = value2
                
#         elif args_list[0] == "MERGE":
#             r1 = int(args_list[1])-1
#             c1 = int(args_list[2])-1
#             r2 = int(args_list[3])-1
#             c2 = int(args_list[4])-1
            
#             if table[r1][c1] != '':
#                 table[r2][c2] = table[r1][c1]
#                 # r = r1
#                 # c = c1
#                 value = table[r1][c1]
#             elif table[r1][c1] == '' and table[r2][c2] != '':
#                 table[r1][c1] = table[r2][c2]
#                 # r = r2
#                 # c = c2
#                 value = table[r2][c2]
            
#             for cell in merge_list:
#                 if (r1, c1) in cell or (r2, c2) in cell:
#                     for curr_r, curr_c in cell:
#                         table[curr_r][curr_c] = value
            
#             for cell in merge_list:
#                 if (r1, c1) in cell and (r2, c2) in cell:
#                     pass
#                 elif (r1, c1) in cell and (r2, c2) not in cell:
#                     cell.append((r2, c2))
#                 elif (r1, c1) not in cell and (r2, c2) in cell:
#                     cell.append((r1, c1))
            
#             merge_list.append([(r1, c1), (r2, c2)])
                
        
#         elif args_list[0] == "UNMERGE":
#             r = int(args_list[1])-1
#             c = int(args_list[2])-1
            
#             ml2 = merge_list.copy()
#             for cell in merge_list:
#                 if (r, c) in cell:
#                     value = table[r][c]
#                     for curr_r, curr_c in cell:
#                         table[curr_r][curr_c] = ''
#                     table[r][c] = value
#                 ml2.remove(cell)
#             ml2 = merge_list
            
            
#         elif args_list[0] == "PRINT":
#             r = int(args_list[1])-1
#             c = int(args_list[2])-1
            
#             if table[r][c] == '':
#                 answer.append('EMPTY')
#             else:
#                 answer.append(table[r][c])
                
    
#     return answer

def solution(commands):
    N = 50 * 50  # total cells (50x50)
    # Initialize union-find parent pointers and value storage.
    parent = list(range(N))
    cell_value = ["" for _ in range(N)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(x, y):
        rx, ry = find(x), find(y)
        if rx == ry:
            return
        parent[ry] = rx
        if cell_value[rx] == "":
            cell_value[rx] = cell_value[ry]
    
    answer = []
    
    for command in commands:
        parts = command.split()
        op = parts[0]
        
        if op == "UPDATE":
            if len(parts) == 4:  
                r, c, new_val = int(parts[1]), int(parts[2]), parts[3]
                idx = (r - 1) * 50 + (c - 1)
                root = find(idx)
                cell_value[root] = new_val
            else: 
                v1, v2 = parts[1], parts[2]
                for i in range(N):
                    if find(i) == i and cell_value[i] == v1:
                        cell_value[i] = v2
        
        elif op == "MERGE":
            r1, c1, r2, c2 = map(int, parts[1:])
            idx1 = (r1 - 1) * 50 + (c1 - 1)
            idx2 = (r2 - 1) * 50 + (c2 - 1)
            # If the same cell, ignore.
            if idx1 == idx2:
                continue
            union(idx1, idx2)
        
        elif op == "UNMERGE":
            r, c = int(parts[1]), int(parts[2])
            idx = (r - 1) * 50 + (c - 1)
            root = find(idx)
            keep_val = cell_value[root]
            group = []
            for i in range(N):
                if find(i) == root:
                    group.append(i)
            for i in group:
                parent[i] = i
                cell_value[i] = ""
            cell_value[idx] = keep_val
        
        elif op == "PRINT":
            r, c = int(parts[1]), int(parts[2])
            idx = (r - 1) * 50 + (c - 1)
            root = find(idx)
            answer.append(cell_value[root] if cell_value[root] else "EMPTY")
    
    return answer