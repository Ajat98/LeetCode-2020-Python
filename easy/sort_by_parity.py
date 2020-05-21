'''
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
'''


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        return [x for x in A if x%2 == 0] + [x  for x in A if x%2 !=0]
