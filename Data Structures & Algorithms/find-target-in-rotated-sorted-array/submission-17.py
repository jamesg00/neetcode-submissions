class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1 
        '''

        l = 0
        r = len(nums) - 1

        while l <= r:

            m = l + (r-l) // 2


            if target == nums[m]:
                return m

            #are we in left portion of array?
            if nums[l] <= nums[m]:
                #is target inside here?
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else:
                # is tagret inside right sorted?
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        
        
        return -1 









            

            











