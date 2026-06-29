class Solution:
    #two pointers are good for finding pair, triplet, or range of elements

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []


        for i in range(len(nums)):

            if i > 0 and nums[i] == nums[i-1]:
                continue

            l = i + 1
            r = len(nums)-1

            while l < r:

                total = nums[i] + nums[l] + nums[r]

                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])


                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1 
                    r -= 1

 

        return res 




    '''
       Time Complexity (On^3)/Space Complexity(Om)
        nums.sort()
        res = set()
        
        n = len(nums)
        for i in range(0, n-2):
            for j in range(i+1, n-1):
                for k in range(j+1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(tuple([nums[i], nums[j], nums[k]]))
        return [list(i) for i in res]
    '''











