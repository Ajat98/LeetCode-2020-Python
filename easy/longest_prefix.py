class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        if not strs: return ''
        maxlen = max([len(x) for x in strs])
        maxstr = max(strs)
        
        longest = ''
        pos = 0
        for i in range(maxlen):
            for w in strs:
                if i < len(w):
                    c = w[i]
                    if c!= maxstr[i]:
                        return longest
                else:
                    return longest

                
            longest += c
            
        
        return longest
                    
                
