class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        #init a bucket with size n for left and right array
        l_arr = [0] * n
        r_arr = [0] * n

        leftMul = 1
        rightMul = 1
        #we set left mul and right mul to 1
        for i in range(len(nums)):
            j = -i - 1
            #init left and right array with
            #indicies to left anf right multiplier      
            l_arr[i] = leftMul
            r_arr[j] = rightMul 
            #multiply multiplier by nums[i] and [j]
            #respectively
            leftMul *= nums[i]
            rightMul *= nums[j]

        #returns the multiplication of each other num on our output
        return [l*r for l,r in zip(l_arr, r_arr)]

