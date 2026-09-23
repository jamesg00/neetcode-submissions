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

        state = {}

        start = 0
        max_ = 0


        for end in range(len(s)):

            state[s[end]] = state.get(s[end], 0) + 1
        

            while state[s[end]] > 1:

                state[s[start]] -= 1
                start += 1
            
            max_ = max(max_, end - start + 1)
        
        return max_ 




        

        









            



