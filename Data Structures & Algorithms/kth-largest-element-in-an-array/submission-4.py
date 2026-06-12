import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #O n log k Time || O (k) space
        '''
        return heapq.nlargest(k, nums)[-1]
        '''


        heap = []

        for num in nums:

            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                heapq.heappushpop(heap, num)
        
        return heap[0]



        








        