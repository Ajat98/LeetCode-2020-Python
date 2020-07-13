#Return bool of whether sentence is a palindrome, only checking alphanumeric characters and ignoring cases


import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        
        s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]
