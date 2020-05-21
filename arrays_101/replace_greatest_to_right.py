'''
Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.
MODIFY IN PLACE
'''

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        
        #Start at the end and work backwards, keep current value
        #Apply list change at the end
        #We want to work on arr[:-1:-1]
            
        l = len(arr)-1
        #used to initialize last item in arr
        greatest = -1
        
        #Start at last index, increment -1
        for i in range(l, -1, -1):
            temp = arr[i]
            arr[i] = greatest
            if temp > greatest:
                greatest = temp
        return arr
            
            
