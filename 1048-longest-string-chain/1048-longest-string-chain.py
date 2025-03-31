class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        dp = {}
        max_chain = 1

        for word in words:
            dp[word] = 1

            for i in range(len(word)):
                predecessor = word[:i] + word[i+1:]
                if predecessor in dp:
                    dp[word] = max(dp[word], dp[predecessor] + 1)
                
            max_chain = max(max_chain, dp[word])

        return max_chain


#         word_by_length = {}
#         max_length = 0
        
#         for word in words:
#             length = len()
#             if length > max_length:
#                 max_length = length

#             if word_by_length.get(length):
#                 word_by_length[length].append(word)
#             else:
#                 word_by_length[length] = [word]
        
#         for i in range(1, max_length+1):
#             if i != max_length:
#                 for word in word_by_length[i]:
#                     for word2 in word_by_length[i+1]:
#                         for i in range(length(word2)):
#                             if word2[:i] + word2[i+1:] == word1:
                                


#         # parent = {}
#         # for word in words:
#         #     for word2 in words:
#         #         if word == word2:
#         #             continue
                
#         #         for i in range(length(word)):
#         #             if word[:i] + word[i+1:] == word2:





                                                                                                                                                                                                                                                                                                                                                                                                                                                                        