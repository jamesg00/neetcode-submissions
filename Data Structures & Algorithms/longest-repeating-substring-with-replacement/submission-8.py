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

        freq_map = {}
        l = 0
        max_freq = 0
        best = 0

        for r in range(len(s)):
            ch = s[r]
            if ch not in freq_map:
                freq_map[ch] = 1
            else:
                freq_map[ch] += 1
            
            max_freq = max(max_freq, freq_map[ch])

            while (r-l+1) - max_freq > k:
                left_ch = s[l]
                freq_map[left_ch] -=1
                l += 1

            best = max(best, r - l + 1)
        return best 

        







            



        