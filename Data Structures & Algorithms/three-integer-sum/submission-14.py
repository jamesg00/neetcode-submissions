class Solution:
    #two pointers are good for finding pair, triplet, or range of elements

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        if not nums: return []

        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):

                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add(tuple([nums[i], nums[j], nums[k]]))
        
        return [list(i) for i in res]






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











