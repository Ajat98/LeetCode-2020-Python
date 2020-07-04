class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        #build steps
        if n == 0: return 0
        if n == 1: return 1
        
        levels = 0
        steps = 0
        count = 0
        while True:
            count += steps + 1
            steps += 1
            if n >= count:
                levels += 1
            else:
                return levels
            
