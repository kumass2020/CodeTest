class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)

        if N == 0:
            return 0
        elif N == 1:
            return 1

        i = 0
        j = 1
        subset = set()
        max_len = -1

        while i < N:
            # subset.add(s[i])
            while j-1 < N and s[j-1] not in subset:
                
                subset.add(s[j-1])
                j += 1
                # print(s[j-1], subset, j < N, s[j-1] not in subset)
            # if j == N-1:
            #     max_len = max(max_len, j-i-1)
            # else:
            # print(i, j, subset)

            max_len = max(max_len, j-i-1)

            # print(i, subset)
            if s[i] in subset:
                subset.remove(s[i])
            i += 1
            
        return max_len
            

