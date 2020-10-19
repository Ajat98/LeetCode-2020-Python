
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        d = {}
        for i, val in enumerate(nums):
            a = target - val
            if a not in d:
                d[val] = i
            else:
                return [d[a], i]
