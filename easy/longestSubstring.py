class Solution:
     def lengthOfLongestSubstring(self, s: str) -> int:
#         start = 0
#         maxLen = 0
#         seen = {}
        
#         for i in range(len(s)):
#             if s[i] in seen and start <= seen[s[i]]:
#                 start = seen[s[i]] + 1
            
#             else:
#                 maxLen = max(maxLen, i - start + 1)
            
#             seen[s[i]] = i
            
#         return maxLen

        #cleaner code

        seen = {}
        max_len, start = 0, 0

        for i, x in enumerate(s):
            if x in seen and start <= seen[x]:
                start = seen[x] + 1
            else:
                max_len = max(max_len, i - start + 1)

            seen[x] = i


        return max_len
