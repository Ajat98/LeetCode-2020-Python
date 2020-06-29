class Solution:
    def removeDuplicates(self, S: str) -> str:
        
        #using stack
        temp = []
        
        for c in S:
            if temp and temp[-1] == c:
                temp.pop()
            else:
                temp.append(c)
                
        return "".join(temp)
    
                    
                
