class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        length = 0
        for num in nums:
            
            if num == 1:
                length += 1
            else:
                length = 0
            
            count = max(count, length )

        return count 

              



        