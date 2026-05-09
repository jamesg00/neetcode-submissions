class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        #which array is shorter?

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        
        #determine total len of combined input arrays
        total_len = len(nums1) + len(nums2)
        half_len = total_len // 2


        l, r = 0, len(nums1)

        while l <= r:
            #partition1
            partition1 = (l+r) // 2
            partition2 = half_len - partition1
            #finx maxes and min of each partition 
            maxL1 = float('-inf') if partition1 == 0 else nums1[partition1-1]
            minR1 = float('inf') if partition1 == len(nums1) else nums1[partition1]

            maxL2 = float('-inf') if partition2 == 0 else nums2[partition2-1]
            minR2 = float('inf') if partition2 == len(nums2) else nums2[partition2]

            if maxL1 <= minR2 and maxL2 <= minR1:
                if total_len % 2 == 0:
                    median = (max(maxL1, maxL2) + min(minR1, minR2)) / 2
                else:
                    median = min(minR1, minR2)

                return median 
            elif maxL2 > minR2:
                r = partition1 - 1
            else:
                l = partition1 + 1











            











        

        