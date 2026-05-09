class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        res = []

        for i in range(len(temperatures)):
            count = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    count = j - i
                    break
            res.append(count)
        return res
'''

        res = [0] * len(temperatures)
        stack = [] #pair [temp, index]

        for i, t in enumerate(temperatures):
            #if todays temperature is warmer than
            #the temperature on thetop of the stack
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t,i))
        return res


