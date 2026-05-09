class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        '''
       
        cS = ""

        for i in range(len(s)):
            if s[i].isalnum():

                cS += s[i]
        
        return cS.lower() == cS[::-1].lower()

        '''

        characters = []

        for char in s:
            if char.isalnum():
                characters.append(char.lower())

        l, r = 0, len(characters)-1

        while l < r:
            if characters[l] != characters[r]: return False

            l += 1
            r -= 1

        return True 
