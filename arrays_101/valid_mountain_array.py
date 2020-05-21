'''
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:
A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
'''

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        if not A: return False
        peak = A.index(max(A)) 
        
        if A == sorted(set(A)) or A[::-1] == sorted(set(A)) or len(A) <3:
            return False
        
        
        #Need to reverse slice with format  A[slice][::-1], reduced errors for some reason.        
        if A[:peak] == sorted(set(A[:peak])) and A[peak:][::-1] == sorted(set(A[peak:][::-1])):
            
            return True
