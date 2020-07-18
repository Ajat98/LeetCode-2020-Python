class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        #Runs out on very long input
        #return list(set([x for x in nums if nums.count(x) > 1]))
        
        d = {}
        for x in nums:
            if x in d:
                d[x] += 1
            else:
                d[x] = 1
                
        return [x for x in d.keys() if d[x]>1]
        
