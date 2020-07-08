class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        #First iteration of a solution, can make it run faster!!
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        for k in range(len(s)):
            a = s[k]
            if d[a] == 1:
                return k
        return -1
            
