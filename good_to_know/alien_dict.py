class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        
        #Logic
        #Get first char of every word
        #If indexes are in increasing order based on their place in the dict, is ordered
        #If first letters are the same, move to next letter
        
        #dict of ordering
        d = {}
        for i, x in enumerate(order):
            d[x] = i
        
        #Will hold indexes of words characters
        transformed = []
        flag = True
        for w in words:
            new = []
            for c in w:
                new.append(d[c])
            transformed.append(new)
            
        for i in range(len(transformed)-1):
            if transformed[i] > transformed[i+1]:
                return False
            
        return True
            
