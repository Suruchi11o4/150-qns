class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Replace the trailing 0s in nums1 with the elements of nums2
        nums1[m:] = nums2
        
        # Sort nums1 in-place
        nums1.sort()