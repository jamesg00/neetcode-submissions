class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        sort = sorted(nums)
        if not sort: return 0
        max_length = 1
        current_length = 1

        for i in range(1, len(sort)):
            if sort[i] == sort[i-1] + 1:
                current_length += 1
            elif sort[i] == sort[i-1]:
                continue
            else:
                max_length = max(max_length, current_length)
                current_length = 1
        
        return max(max_length, current_length)
            


            

