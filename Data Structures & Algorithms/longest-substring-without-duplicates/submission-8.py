class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        '''
        n is len of string, m is total number of unique chars in string 
        O(n*m) Time || O(1) Space 
        ======================================
        count = 0
        for i in range(len(s)):
            track = set()
            for j in range(i, len(s)):
                if s[j] in track: 
                    break
                track.add(s[j])
                #we use len track because = length of 
                #substring from i up to just before duplicate
            count = max(count, len(track))
        return count 
        '''

        mp = {}
        l = 0
        res = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]] + 1, l)
            mp[s[r]] = r
            res = max(res, r-l+1)
        return res 

        mp = {}
        l = 0
        res = 0






            



