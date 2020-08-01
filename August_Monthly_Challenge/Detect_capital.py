#https://leetcode.com/problems/detect-capital/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #Three cases to check
        #Capital only at first letter
        #Capital every letter
        #no capitals
        
        caps = 0
        for c in word:
            if c == c.upper():
                 caps += 1
                
        return caps == 0 or (caps == 1 and word[0] == word[0].upper()) or caps == len(word)
    
    
        #ADDITIONALLY, useful python methods include.
        return word.isupper() or word.islower() or word.istitle()
            
