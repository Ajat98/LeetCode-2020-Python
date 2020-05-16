class Solution:
    def isValid(self, s: str) -> bool:
        
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('[]', '').replace('{}','')
    
        if s == '': return True
        else: return False
        
        #Not very time or space efficient, there are better ways to do this.
