'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
'''

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        #Start and end pos
        s = 0
        e = len(A) -1
        
        while s < e:
            #check start end points for even/odd, if s is even move s + 1, if e is odd move e -1
            while A[s] % 2 == 0 and s < e:
                s +=1
            while A[e] % 2 == 1 and s < e:
                e -=1
            A[s], A[e] = A[e], A[s]

            
                
        return A
        
