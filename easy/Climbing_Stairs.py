class Solution:
    def climbStairs(self, n: int) -> int:
        
        dp = [0]*(n+1) #will store num of steps to reach  a certain step 
        
        if n == 0: return 0
        if n == 1: return 1
        
        dp[1] = 1
        dp[2] = 2
            
        #From i'th step, i-1 is taking 1 step from the step before it
        #i-2 accounts for taking 1 step of size 2 from the step 2 before it
        for i in range(3, n+1):
            dp[i] = dp[i -1] + dp[i-2]
      
        return dp[n]
        
