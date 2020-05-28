"""
Given a non-empty array of integers, return the third maximum number in this array.
If it does not exist, return the maximum number. The time complexity must be in O(n).
Note: Distinct max only
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

"""

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(set(nums)) < 3:
            return max(nums)
        
        #Distinct only
        nums = sorted(list(set(nums)))
        print(nums)
        for i in range(2):
            nums.pop()
        return max(nums)  
        
