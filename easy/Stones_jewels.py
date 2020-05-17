class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        
        #Very slow runtime
        count = 0
        for i in S:
            if i in J:
                count += 1
        return count
            
        
