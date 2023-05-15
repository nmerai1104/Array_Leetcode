class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mg= sorted(nums1 + nums2)
        mgLen = len(mg)
        index = (mgLen - 1) // 2
        if (mgLen % 2):
            return mg[index]
        else:
            return (mg[index] + mg[index + 1])/2.0        
