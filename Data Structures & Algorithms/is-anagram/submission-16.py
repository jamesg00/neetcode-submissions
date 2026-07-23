class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(t) != len(s): return False

        hashT, hashS = {}, {}

        for i in range(len(s)):
            hashS[s[i]] = hashS.get(s[i], 0) + 1
            hashT[t[i]] = hashT.get(t[i], 0) + 1

        return hashS == hashT 
        
