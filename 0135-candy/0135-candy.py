class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)
        for i, r in enumerate(ratings):
            # candies[i] += 1

            if i >= 1:
                if ratings[i-1] > ratings[i] and candies[i-1] <= candies[i]:
                    candies[i-1] += 1
                elif ratings[i-1] < ratings[i]:
                    candies[i] = max(candies[i], candies[i-1]+1)

        for i in range(len(ratings), -1, -1):
            if i+1 <= len(ratings)-1:
                if ratings[i+1] > ratings[i] and candies[i+1] <= candies[i]:
                    candies[i+1] += 1
                elif ratings[i+1] < ratings[i]:
                    candies[i] = max(candies[i], candies[i+1]+1)

        # print(candies)
        return sum(candies)
            
