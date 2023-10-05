#find the minimum cost to reach the top
#can start from index 1 or index 0
#use decision tree to visualize

class Solution:
    def minCostClimbinStairs(self, cost:List[int])->int:

        cost.append(0)
        for i in range (len(cost)- 3, -1, -1):
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])

        return min(cost[0], cost[1])