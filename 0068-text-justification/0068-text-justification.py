class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        N = len(words)

        i = 0
        answer = []
        while i < N:
            line = ''

            # print(i)
            word = words[i]
            total_length = len(word)
            end_idx = -21
            for j in range(i+1, N):
                total_length += len(words[j])+1

                if total_length > maxWidth:
                    total_length -= len(words[j])+1
                    end_idx = j-1
                    break
                else:
                    end_idx = j

            res = maxWidth - total_length
            words_num = end_idx-i+1
            if i == end_idx or i == N-1:
                # left-justified
                line = word + ' ' * res
            elif i != end_idx and end_idx == N-1:
                for j in range(i, end_idx+1):
                    word = words[j]
                    if j == i:
                        line += word
                    else:
                        line += ' ' + word
                    
                    if j == end_idx:
                        line += ' ' * res


            elif end_idx != -21 and words_num > 1:
                # fully justified
                # words_num = end_idx-i+1

                _res = res + words_num-1
                count = words_num-1
                avg = (res + words_num - 1) // (words_num-1)
                is_even = False if res % (words_num-1) else True
                # print(res % (words_num-1))

                for j in range(i, end_idx+1):
                    # print(is_even, _res, count * avg)
                    word = words[j]
                    if j == i:
                        line += word
                    else:
                        if not is_even and words_num > 1 and _res > count * avg:
                            spaces = ((res // (words_num-1))+1) + 1
                        else:
                            spaces = ((res // (words_num-1))+1)
                        # print("spaces:",spaces)
                        count -= 1
                        _res -= spaces
                        line += ' ' * spaces + word  

            i = max(i+1, end_idx+1)
            answer.append(line)

        return answer

