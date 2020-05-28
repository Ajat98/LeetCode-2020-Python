"""
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        #Need a faster way to do this.
        #check = [i for i in range(1, len(nums)+1)]
        #print(check)
        #return [x for x in check if x not in nums]
        
        #Still too slow for large inputs
        # missing = []
        # top = len(nums) +1
        # for i in range(1, top):
        #     if i not in nums:
        #         missing.append(i)
        #     if top-i not in nums:
        #         missing.append(top-i)
        # return list(set(missing))
    
    
        for i in nums:
            x = abs(i) - 1
            
            #Change index of num in list to a negative val if positive
            if nums[x] > 0: 
                nums[x] *= -1
        
        #i+1 since nums start at 1
        #Non negative vals left over will be missing nums
