import math

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
    
        #return ((math.log(num) / math.log(4)) == (math.floor(math.log(num) / math.log(4)) * 1.0))
        
        if num <= 0: return False
        return math.log(num, 4).is_integer()
        
