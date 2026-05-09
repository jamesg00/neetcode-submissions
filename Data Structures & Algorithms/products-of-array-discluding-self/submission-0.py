class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        leftMul = 1
        rightMul = 1

        for i in range(len(nums)):
            j = -i - 1

            l_arr[i] = leftMul
            r_arr[j] = rightMul 

            leftMul *= nums[i]
            rightMul *= nums[j]

        return [l*r for l,r in zip(l_arr, r_arr)]

