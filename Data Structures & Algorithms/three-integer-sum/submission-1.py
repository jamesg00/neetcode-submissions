class Solution:
    #two pointers are good for finding pair, triplet, or range of elements
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       #brute force solution


        #we can actually make a better ON solutiong using two pointers
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            #once a is positive, 3 positives cant sum to zero
            if a > 0 : break
            #duplicates
            if i > 0 and a == nums[i-1]: continue
            l, r = i+1, len(nums)-1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1

                elif threeSum > 0:
                    r -= 1
                else:
                    res.append([a,nums[l],nums[r]])
                    #remember to decremenet l and r
                    l += 1
                    r -= 1
                    #if we have duplicates and l is less than n
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
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











