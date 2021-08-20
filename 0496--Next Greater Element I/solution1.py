class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        temp = {}
        for i in range(len(nums1)):
            temp[nums1[i]] = i

        result = [-1 for _ in range(len(nums1))]

        stack = []

        for i in range(len(nums2) - 1, -1, -1):
            while len(stack) != 0 and nums2[i] >= stack[-1]:
                stack.pop()

            if nums2[i] in temp:
                if len(stack) == 0:
                    temp2 = -1
                else:
                    temp2 = stack[-1]
                result[temp[nums2[i]]] = temp2

            stack.append(nums2[i])
        return result