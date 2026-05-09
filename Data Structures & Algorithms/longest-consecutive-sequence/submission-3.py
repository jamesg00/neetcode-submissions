class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
       # i create nums sorted to be able to search in index
       
        sort = sorted(nums)
        #base case and init length vars
        #curernt length for i length
        #max length to the maximum found at the time
        if not sort: return 0
        max_length = 1
        current_length = 1

       #start from 1 to len sort
       #add current length is sort[i] == sort[i-1] + 1
        for i in range(1, len(sort)):
            if sort[i] == sort[i-1] + 1:
                current_length += 1
            #you need to check if there are duplicates
            elif sort[i] == sort[i-1]:
                continue
            else:
            #save our maximum length if we break out of
            #equivalence loop and make cur length 1 again
                max_length = max(max_length, current_length)
                current_length = 1
        
        return max(max_length, current_length)
            
'''
#o n log n time 
because sorting (sorted = ...) take o n log n
we only care about the dominant (bigger) term

o n space
because we intialize sorted as the sort of n elements         
'''
