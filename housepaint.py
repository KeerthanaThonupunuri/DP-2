#Executed on leet code
#time complexity - O(n)
#space compleexity - O(1)
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        if(n==0) : return 0
        for i in range(1,n):
            costs[i][0] += min(costs[i-1][1],costs[i-1][2])
            costs[i][1] += min(costs[i-1][0],costs[i-1][2])            
            costs[i][2] += min(costs[i-1][1],costs[i-1][0])            
        return min(costs[-1])
        