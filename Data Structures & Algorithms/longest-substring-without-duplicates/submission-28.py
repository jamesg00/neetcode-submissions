class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        state = {}
        start = 0
        maxx = 0

        for end in range(len(s)):

            state[s[end]] = state.get(s[end], 0) + 1


            while state[s[end]] > 1:

                state[s[start]] -= 1
                start += 1
            
            maxx = max(maxx, end - start + 1)
        
        return maxx 



            
        