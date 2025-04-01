class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        T = len(cost)
        agg_cost = [0 for i in range(T)]

        agg_cost[0] = cost[0]
        agg_cost[1] = cost[1]

        for i in range(2, T):
            agg_cost[i] = cost[i] + min(agg_cost[i-1], agg_cost[i-2])

        return min(agg_cost[T-1], agg_cost[T-2])