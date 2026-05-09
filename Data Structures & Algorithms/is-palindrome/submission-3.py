class Solution:
    def isPalindrome(self, s: str) -> bool:

        newString = ""

        for i in range(len(s)):
            if s[i].isalnum(): 
                newString += s[i]

        return newString.lower() == newString.lower()[::-1]




