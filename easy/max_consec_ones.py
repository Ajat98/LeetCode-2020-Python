#Given a binary array, find the maximum number of consecutive 1s in this array.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        high = 0
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp += 1
            else:
                temp = 0
            if high < temp:
                high = temp
        return high
                
