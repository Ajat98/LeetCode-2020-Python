class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        #If a letter going from right to left is less than its next letter, it will be subtracted.
        #last letter always added
        total = 0
        for i in range(len(s)-1):
            if d[s[i]] < d[s[i+1]]:
                total -= d[s[i]]
            else:
                total += d[s[i]]
            print(total)
        return total + d[s[-1]]
