#Usefull video explaining algo used. https://www.youtube.com/watch?v=jaNZ83Q3QGc

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        combinations = (amount+1) * [0]
        
        #only way to make zero coins is with no coins, count this as 1
        combinations[0] = 1
        
        for coin in coins:
            for i in range(len(combinations)):
                if i >= coin:
                    combinations[i] += combinations[i-coin]
                    
                    
                    
        return combinations[amount]
        
       
       
