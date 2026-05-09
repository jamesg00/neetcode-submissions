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

        max_freq = {}
        l = 0
        max_count = 0
        best_window_count = 0

        for r in range(len(s)):
            r_ch = s[r]

            if r_ch not in max_freq:
                max_freq[r_ch] = 1
            else:
                max_freq[r_ch] += 1
            
            max_count = max(max_count, max_freq[r_ch])

            while (r-l+1) - max_count > k:
                l_ch = s[l]
                max_freq[l_ch] -= 1
                l += 1
            
            best_window_count = max(best_window_count, r-l+1)
        
        return best_window_count 






            









            



        