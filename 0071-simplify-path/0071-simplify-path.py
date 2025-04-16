class Solution:
    def simplifyPath(self, path: str) -> str:
        path_lst = path.split("/")
        # print(path_lst)

        simp_list = []
        
        for i, p in enumerate(path_lst):
            # if i >= 1 and p == '' and path_lst[i-1] != '':
            #     continue
            # if i == len(path_lst)-1 and p == '':
            #     continue
            # if i == 0:
            #     simp_list.append('/')

            if p == '':
                continue
            elif p == '.':
                continue
            elif p == '..':
                if simp_list:
                    simp_list.pop()
                continue
                # if simp_list:
                #     simp_list.pop()
            else:
                p = '/' + p
            # elif p == '':
                # p = '/'

            simp_list.append(p)
        return ''.join(simp_list) if simp_list else '/'