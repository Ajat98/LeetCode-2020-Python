class Solution:
    def isPalindrome(self, x: int) -> bool:
       
        '''OPTIMIZE IT MORE: Only an inplace optimization without using String conversion'''
        a, b = x, 0
        n = lambda: (b*10) + (a%10)
        while a > 0:
            a, b = a // 10, n()
        return b == x
    
        
        
        
        
        '''
        #WITH STRING CONVERSION
        first_char = ''
        if str(x)[0] == '-':
            return False
        
        else:
            return int(str(x)[::-1]) == x
        '''
        
        
