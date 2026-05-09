class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        '''
        BruteForce Approach
        #O(n^2) Time || O(m) space
        #n is len of string, m is number of unique characters in string
        res = 0

        for i in range(len(s)):
            mp = {}
            maxF = 0

            for j in range(i, len(s)):
                mp[s[j]] = 1 + mp.get(s[j], 0)
                maxF = max(maxF, mp[s[j]])

                if (j-i+1) - maxF <= k:
                    res = max(res, j-i+1)
        return res 
        '''

        #count occurence of each char
        count = {}
        #longest substring we can create
        res = 0

        l = 0

        for r in range(len(s)):
            #grows the window
            count[s[r]] = 1 + count.get(s[r], 0)

            #this checks if our window size is longer than k
            #which means window is invalid so we dec count of s[l] and incremement l pointer
            while (r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1


            #return the max of res or 
            #size of window (r-l+1)
            res = max(res, r-l+1)
        return res 


            



        