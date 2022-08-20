class Solution:
    def climbStairs(self, n):
        def climb(n, memo):
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            if memo.get(n):
                return memo[n]
            
            memo[n] = climb(n-1, memo) + climb(n-2, memo) 
            return memo[n]
        
        return climb(n, {})