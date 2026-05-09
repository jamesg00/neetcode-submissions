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
            m = (l+r) // 2

            if target == nums[m]:
                return m

            
            #is left half sorted?
            if nums[l] <= nums[m]:
                #is the target inside that sorted half?
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            
            else:
                #does target belong in sorted right half?
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1 








