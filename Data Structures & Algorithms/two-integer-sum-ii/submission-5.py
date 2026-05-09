class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #Two Pointer Approach


        l = 0
        r = len(numbers) - 1

        #While we are in bounds we definec current sum and check conditions against target
        #if current greater r decrements, else if current less l increments
        #returns [l+1,r+1], end of while loop return []
        while l < r:
            currentSum = numbers[l] + numbers[r]

            if currentSum > target:
                r -= 1
            elif currentSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return [] 



