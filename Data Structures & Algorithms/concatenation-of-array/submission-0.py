class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res =[]
        n = len(nums)
        i = 0

        while len(res) < n * 2:
            if i <= len(nums) -1:
                res.append(nums[i])
                i += 1
            elif i == len(nums):
                i = 0
            else:
                res.append(nums[i])

        return res 

        