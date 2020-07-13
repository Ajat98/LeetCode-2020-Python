#Find only instance of item in list that does not repeat.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        #BITWISE SOLUTION
        '''
        r = 0
        for i in nums:
            #any num XOR'd equals with itself cancels out and equals 0:
            #e.g.  1^1 = 0, (1^1)^2 = 2.
            r ^= i
            
        return r
        '''
        
        #Faster solution using lambda - Fasted solution
        return reduce(lambda x,y: x^y, nums)
        
        
        #using operator.xor, SLOWER THAN LAMBDA
        #return reduce(operator.xor, nums)
    
        #HASHMAP - Slower than lambda as well
        '''
        d = {}
        
        for i in nums:
            d[i] = d.get(i, 0)+1
            
        for k, v in d.items():
            if v == 1:
                return k
        '''
