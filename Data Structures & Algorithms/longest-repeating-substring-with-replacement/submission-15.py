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

        max_freq = 0
        state = {}
        longest = 0
        start = 0

        for end in range(len(s)):
            state[s[end]] = state.get(s[end], 0) + 1

            max_freq = max(max_freq, state[s[end]])

            if k + max_freq < end - start + 1:
                state[s[start]] -= 1
                start += 1

            longest = max(longest, end - start + 1)
        
        return longest 






            









            



        