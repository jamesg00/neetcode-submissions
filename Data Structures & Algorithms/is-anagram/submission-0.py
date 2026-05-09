class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #string case in which if the lengths dont match it returns false
        if len(s) != len(t):
            return False 

        #initialize hashmaps
        stringS = {}
        stringT = {}

        #incrememnt through range len s, then append chars to stringS and stringT
        for i in range(len(s)):
            #for each i, get all indicies of chars from T and S using .get, otherwise it will default to 0
            stringS[s[i]] = 1 + stringS.get(s[i], 0)
            stringT[t[i]] = 1 + stringT.get(t[i], 0)

        
        for x in stringS:
            if stringS[x] != stringT.get(x,0):
                return False


        return True


        




        