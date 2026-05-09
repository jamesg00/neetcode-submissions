class Solution:
    def isPalindrome(self, s: str) -> bool:

        #first we have to check for any alpha numeric chars
        #then we append to this char stack
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char.lower())
        
        #two pointer approach
        l , r = 0 , len(chars) - 1

        
        #while l < r, check if any opposite values are not same
        #if not then its autmatically false
        #if so, it will keep incerment/decremeing l and r
        #then return True if we get out of while loop
        
        while l < r:
            if chars[l] != chars[r]:
                return False
            
            l += 1
            r -= 1
            
        return True
   

        