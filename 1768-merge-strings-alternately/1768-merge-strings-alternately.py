class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge_len = min(len(word1), len(word2))
        max_len = max(len(word1), len(word2))
        answer = ''
        long_one = ''
        # print(len(word1) <= len(word2))
        if len(word1) > len(word2):
            long_one = word1
        else:
            long_one = word2

        for i in range(merge_len):
            answer += word1[i] + word2[i]

        for i in range(merge_len, max_len):
            # print(i)
            # print(len(word1))
            # print(len(word2))
            # print(word1)
            # print(word2)
            # print(long_one)
            answer += long_one[i]
                
        return answer