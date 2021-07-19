class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = []
        for i in range(k):
            result.append(nums[i])

        for j in range((k - 2) // 2, -1, -1):
            sift(result, j, k - 1)

        for m in range(k, len(nums)):
            if nums[m] > result[0]:
                result[0] = nums[m]
                sift(result, 0, k - 1)

        return result[0]


def sift(li, low, high):
    i = low
    j = 2 * i + 1
    while j <= high:
        if j + 1 <= high and li[j + 1] < li[j]:
            j = j + 1
        if li[i] > li[j]:
            li[i], li[j] = li[j], li[i]
            i = j
            j = 2 * i + 1
        else:
            break