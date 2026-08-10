class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        res = []
        for i in range(len(arr)):
            maxx = 0
            j = i + 1
            for k in range(j, len(arr)):
                maxx = max(maxx, arr[k])
            res.append(maxx)
        r = len(res)-1
        res[r] = -1
        return res 
            




                

        