class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            track = set()
            for j in range(i, len(s)):
                if s[j] in track: 
                    break
                track.add(s[j])
            count = max(count, len(track))
        return count 

            



