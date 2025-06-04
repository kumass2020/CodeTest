from collections import defaultdict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0

        for s in range(1, amount+1):
            for c in coins:
                if c <= s:
                    dp[s] = min(dp[s], dp[s-c]+1)
            
        return dp[amount] if dp[amount] != amount+1 else -1

        # if not amount:
        #     return 0

        # coins.sort(reverse=True)
        
        # memo = defaultdict(list)
        # # answer = float('inf')
        # answer = 0
        # def dfs(total, count):
        #     nonlocal answer

        #     if answer:
        #         return

        #     for num in coins:
        #         total += num
        #         count += 1

        #         # print(total, count)
                
        #         if total <= amount and not memo[(total, count)]:
        #             memo[(total, count)] = True
                    
        #             if total == amount:
        #                 # answer = min(answer, count)
        #                 answer = count
                    
        #             dfs(total, count)
                    
                
        #         total -= num
        #         count -= 1

        # dfs(0, 0)

        # # return answer if answer != float('inf') else -1
        # return answer if answer else -1
        
