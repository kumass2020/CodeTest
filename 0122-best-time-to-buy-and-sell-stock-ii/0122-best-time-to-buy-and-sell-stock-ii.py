class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = 10001
        max_profit = 0
        answer = 0
        for i in range(len(prices)):
            price = prices[i]
            
            if price < min_price:
                min_price = price
            if max_profit < price - min_price:
                max_profit = price - min_price

            # print(price, min_price, prices[i+1], max_profit)
            if i != len(prices)-1:
                if price > min_price and price > prices[i+1]:
                    answer += max_profit
                    min_price = 10001
                    max_profit = 0
            else:
                answer += max_profit

            
            
        return answer