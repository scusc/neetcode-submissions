class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1, n2 = len(nums1), len(nums2)

        start, end = 0, n1

        while start <= end:
            cut1 = start + (end - start) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1 

            left1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            right1 = float('inf') if cut1 == n1 else nums1[cut1]

            left2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            right2 = float('inf') if cut2 == n2 else nums2[cut2]

            if left1 <= right2 and left2 <= right1:
                if (n1 + n2) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            
            elif left1 > right2:
                end = cut1 - 1
            else:
                start = cut1 + 1
