class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = nums1[:m]
        i = 0
        j = 0
        k = 0
        while k < len(nums1) and i < len(tmp) and j < len(nums2):
            if tmp[i] <= nums2[j]:
                nums1[k] = tmp[i]
                i += 1
            else:
                nums1[k] = nums2[j]
                j += 1
            k += 1
        
        while i < len(tmp):
            nums1[k] = tmp[i]
            i += 1
            k += 1
        while j < len(nums2):
            nums1[k] = nums2[j]
            j += 1
            k += 1
        
         