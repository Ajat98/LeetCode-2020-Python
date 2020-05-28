class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
            
        """
        #Current Solution is too slow
        flipped = 1
        longest = 0
        count = 0
        zeroes = [i for i,x in enumerate(nums) if x ==0]
        #print(zeroes)
        
        if 0 not in nums:
            return len(nums)
        
        for n in zeroes:
            nums[n] = 1
            for i in range(len(nums)):
                if nums[i] == 1:
                    count += 1
                else:
                    count = 0
                if count > longest:
                    longest = count
            nums[n] = 0
        
        return longest
        """      
        
        #MORE EFFICIENT SOLUTION
        #Keep track of previous, current length of consec 1s
        
        prev, curr, highest = -1, 0, 0
        
        for x in nums:
            if x == 0:
                prev, curr, = curr, 0
            else:
                curr += 1
            highest = max(highest, prev +1 + curr)
        
        return highest
            
                
    
            
