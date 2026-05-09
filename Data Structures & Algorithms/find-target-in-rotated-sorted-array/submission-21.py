class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1 
        '''
        l, r = 0, len(nums)-1
        while l <= r:
            m = l + (r-l) // 2
            
            if target == nums[m]:
                return m

            #are we in our left half portionof array
            if nums[l] <= nums[m]:
                #if the target inside of this left portion
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # we are in the right portion of array 
            else:
                #is target inside of the right portion?
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1 


