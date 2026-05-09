class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        O(n) Time O(1) Space
        return min(nums)
        '''

        l = 0 
        r = len(nums) - 1
        cur_ans = nums[0]

        while l <= r:
            if nums[l] < nums[r]: 
                cur_ans = min(cur_ans, nums[l])
                break 

            m = (l+r) // 2
            cur_ans = min(cur_ans, nums[m])

            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return cur_ans 





            
            