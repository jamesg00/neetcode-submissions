class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        cS = ""

        for i in range(len(s)):
            if s[i].isalnum():

                cS += s[i]
        
        return cS.lower() == cS[::-1].lower()