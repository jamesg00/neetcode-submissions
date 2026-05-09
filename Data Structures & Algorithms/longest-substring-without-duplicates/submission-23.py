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


        #O(n) Time ||| O(1) Space 
        char_count = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in char_count:
                char_count.remove(s[l])
                l += 1
            char_count.add(s[r])
            res = max(res, r-l+1)
        return res 

        

        









            



