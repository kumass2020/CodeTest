class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        N = len(words)
        M = len(words[0])
        P = len(s)

        # words_dict = set(words)
        answer = []

        words_dict = {}
        for word in words:
            if words_dict.get(word):
                words_dict[word] = words_dict.get(word) + 1
            else:
                words_dict[word] = 1

        for i in range(P-M*N+1):
            j = i
            substr = s[i:i+M]
            used = {}
            while j < P and substr in words:
                if used.get(substr, 0) > words_dict[substr]:
                    break

                # used.add(substr)
                used[substr] = used.get(substr, 0) + 1
                # print(used, words_dict)

                if used == words_dict:
                    # print('here')
                    answer.append(i)
                    break

                j += M
                substr = s[j:j+M]

        return answer

