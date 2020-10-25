class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = []
        
        for i in range(1, len(nums)+1):
            total.append(sum(nums[0:i]))
        return total
