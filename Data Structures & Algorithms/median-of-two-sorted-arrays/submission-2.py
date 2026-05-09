class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        res = []

        for i in range(len(nums1)):
            res.append(nums1[i])
        
        for j in range(len(nums2)):
            res.append(nums2[j])

        sort = sorted(res)

        n = len(sort)

        if n % 2 == 1:
            med = sort[n//2]
        else:
            med = (sort[n//2-1] + sort[n//2]) / 2
        

        return med

            











        

        