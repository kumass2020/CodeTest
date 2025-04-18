class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        start = 0
        cur_gas = 0
        total_gas = 0
        for i in range(len(gas)):
            cur_gas += gas[i] - cost[i]
            total_gas += gas[i] - cost[i]

            if cur_gas < 0:
                cur_gas = 0
                start = i+1
            
        return start if total_gas >= 0 else -1


        # # if len(gas) == 1:
        # #     return 0
        
        # lst = [0] * len(gas)
        # lst2 = [0] * len(gas)
        # start = 0
        # min_acc = 0
        # min_idx = 0

        # for i in range(len(gas)):
        #     lst[i] = gas[i] - cost[i]
        #     lst2[i] = lst2[i-1] + lst[i] if i >= 1 else lst[i]

        #     if min_acc > lst2[i]:
        #         min_acc = lst2[i]
        #         min_idx = i

        #     if i >= 1 and lst[i-1] < 0 and lst[i] >= 0 and min_idx == i-1:
        #         start = i
                
                
        
        # if sum(lst) < 0:
        #     return -1
            
        # return start