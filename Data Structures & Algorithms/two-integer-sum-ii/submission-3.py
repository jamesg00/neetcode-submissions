class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        #Two pointer approach
        #define left anf right as left and right sides of array

        l, r = 0, len(numbers) - 1
        #whiel we are in bounds, we define current sum which is numbers l + r
        #if currentsum is greater than target, we decrement r
        #else if its less than target we increment i
        
        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                #reaches a case to return the indicies that reach target
                return [l + 1, r + 1]
        return []
        


