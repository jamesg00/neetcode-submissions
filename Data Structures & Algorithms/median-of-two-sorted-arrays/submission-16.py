class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        l = 0 
        r = len(nums1)

        while l <= r:
            p1 = (l+r) // 2
            p2 = half - p1

            maxL1 = float('-inf') if p1 == 0 else nums1[p1-1]
            minR1 = float('inf') if p1 == len(nums1) else nums1[p1]

            maxL2 = float('-inf') if p2 == 0 else nums2[p2-1]
            minR2 = float('inf') if p2 == len(nums2) else nums2[p2]

            if maxL1 <= minR2 and maxL2 <= minR1:
                if total % 2 == 0:
                    median = (max(maxL1, maxL2) + min(minR1 ,minR2)) / 2
                else:
                    median = min(minR1, minR2)
            
                return median 
            elif maxL2 > minR2:
                r = p1-1
            else:
                l = p1 + 1
