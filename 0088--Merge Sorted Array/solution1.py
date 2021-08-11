class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return

        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        for i in range(m - 1, -1, -1):
            nums1[i + n] = nums1[i]

        left = n
        right = 0
        pos = 0

        while left < m + n and right < n:

            if nums1[left] <= nums2[right]:
                nums1[pos] = nums1[left]
                pos += 1
                left += 1
            else:
                nums1[pos] = nums2[right]
                pos += 1
                right += 1
        if left == m + n:
            pos = -1
            for i in range(n - 1, right - 1, -1):
                nums1[pos] = nums2[i]
                pos -= 1

