class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Brute force approach 
        
        output = []

        for i in range(len(nums) - k + 1):
            maxi = nums[i]
            for j in range(i, i + k):
                maxi = max(maxi, nums[j])
            output.append(maxi)

        return output

        
        Right: I got the outpt right, I also did a nested loop which was what we were supposed to do
                I also correctly did the max concept, but not in the right way. 
        Wrong: I didnt realize that I was supposed to keep track of len of nums
               considering k. So when we use a brute force approach i need to len nums - k + 1
               My approach to counting max was wrong. I didnt iterate corretly thru array
               I also throulve make maxI = nums[i]. I was confused and i mistakened
               the max for the max count. Thats why i wrote count[nums[i]]. I need to read
               the prob;em more carfully so i dont go down a deep rabbit hole 
               I also tried to shrink window once l >= k which was wrong. 
        '''
        

        #Right Approach (Queue)
        output = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            #pop smaller values from q
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            #remove the left value from window
            if l > q[0]:
                q.popleft()

            if r+1 >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output 









        