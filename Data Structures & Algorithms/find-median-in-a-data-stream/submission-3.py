import heapq
class MedianFinder:

    def __init__(self):
        self.bot = []
        self.top = []
        
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.bot, -num)
        heapq.heappush(self.top, -heapq.heappop(self.bot))


        if len(self.top) > len(self.bot):

            heapq.heappush(self.bot, -heapq.heappop(self.top))
    


    def findMedian(self) -> float:

        if len(self.bot) != len(self.top):
            return -self.bot[0]
        else:
            return (self.top[0] - self.bot[0]) / 2


        
        