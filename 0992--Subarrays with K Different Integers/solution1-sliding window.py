class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return subarray_k(k, nums) - subarray_k(k - 1, nums)


def subarray_k(k, li):
    dict_count = {}

    i = 0
    result = 0
    curr_k = 0
    for j in range(len(li)):
        if dict_count.get(li[j], 0) == 0:
            curr_k += 1
        dict_count[li[j]] = dict_count.get(li[j], 0) + 1
        while curr_k > k:
            dict_count[li[i]] -= 1
            if dict_count[li[i]] == 0:
                curr_k -= 1
            i += 1
        result += j - i + 1
    return result

