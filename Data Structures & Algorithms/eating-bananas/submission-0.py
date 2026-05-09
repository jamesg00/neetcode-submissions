class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #O (max(p) * p) where p is the length of piles

        #To improve it We can make O(log(max(p)*p))
        #l is 1 and r is our max of piles 
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/k)
            
            if hours <= h:
                res = min(res, k) 
                r = k - 1
            else:
                l = k + 1
        
        return res

                

        

