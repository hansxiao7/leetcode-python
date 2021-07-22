class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = list(set(tuple(nums1)))
        nums2 = list(set(tuple(nums2)))

        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        nums1.sort()
        nums2.sort()

        result = []
        left = 0
        for i in range(len(nums1)):
            temp = binary_search(nums2, 0, len(nums2) - 1, nums1[i])
            if temp != -1:
                result.append(nums2[temp])
                left = temp

        return result


def binary_search(li, left, right, target):
    if left < right:
        mid = (left + right) // 2
        if li[mid] < target:
            return binary_search(li, mid + 1, right, target)
        else:
            return binary_search(li, left, mid, target)

    else:
        if target == li[left]:
            return left
        else:
            return -1