from itertools import permutations
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount+1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i-coin]

        return dp[amount]


        # #  p = permutations(coins)
        # #  print([_p for _p in p])

        # answer = 0 
        # coins.sort(reverse=True)
        # cur_coins = []

        # def dfs(idx):
        #     nonlocal answer, cur_coins

        #     print(cur_coins)

        #     total = sum(cur_coins)
        #     if total == amount:
        #         answer += 1
        #         return
        #     elif total > amount:
        #         return
            
        #     for i in range(idx, len(coins)):
        #         cur_coins.append(coins[i])
        #         dfs(i)
        #         cur_coins.pop()
            
        # dfs(0)
        # return answer