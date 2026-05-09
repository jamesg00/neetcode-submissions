class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Time is O(n+m), Space O(1)

        '''
        if len(s) != len(t): return False 
        
        hash1 = {}
        hash2 = {}


        for i in range(len(s)):
            hash1[s[i]] = 1 + hash1.get(s[i],0)
            hash2[t[i]] = 1 + hash2.get(t[i],0)

        return hash1 == hash2

        '''
        '''
        sortS = sorted(s)
        sortT = sorted(t)

        if len(s) != len(t):
            return False

        for i in range(len(sortS)):
            if sortS[i] != sortT[i]:
                return False
        return True 
    
        O n log n, Space O N

        '''

        if len(s) != len(t) : return False

        hashS = {}
        hashT = {}

        for i in range(len(s)):
            hashS[s[i]] = 1 + hashS.get(s[i], 0)
            hashT[t[i]] = 1 + hashT.get(t[i], 0)

        return hashS == hashT


    
        
