class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        d = {}
        
        for w in strs:
            x = "".join(sorted(w))
            if x in d:
                d[x].append(w)
            else:
                d[x] = [w]
                
        return list(d.values())
            
            
                
