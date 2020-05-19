'''
Given an array arr of integers, check if there exists two integers N and M such that N is the double of M ( i.e. N = 2 * M).
More formally check if there exists two indices i and j such that :
i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
'''

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        doubles = []
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[j] == arr[i]*2 and i != j:
                    return True
                
           
