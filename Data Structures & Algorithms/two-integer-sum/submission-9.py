class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        '''
        for i in range(len((nums))):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
        '''
        '''
        #O(n) time and space

        seen = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]

            seen[n] = i
                
        '''
        seen = {}

        for i, n in enumerate(nums):

            diff = target - n

            if diff in seen:
                return [seen[diff], i]
            
            seen[n] = i

    





            

                    