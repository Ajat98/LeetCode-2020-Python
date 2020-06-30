class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        banned = set(banned)
        #useing regex.
        words = re.findall(r'\w+', paragraph.lower())
        #target words to search for.
        counts = {}
        
        for w in words:
            if w not in banned:
                if w not in counts:
                    counts[w] = 1
                else:
                    counts[w] += 1
                    
        #return key with highest value pair
        max_val = max(counts, key=counts.get)
        return max_val
       
        
       
        
