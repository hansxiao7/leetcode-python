class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        def binary_search(low, high):
            if high - low > 10 ** (-5):
                mid = (low + high) / 2.0
                temp = check_val(nums, mid, k)
                if temp:
                    return binary_search(mid, high)
                else:
                    return binary_search(low, mid)
            else:
                return low

        return binary_search(min(nums), max(nums))


def check_val(nums, target, k):
    temp = [0]
    curr_min = 0
    total = 0
    for i in range(k - 1):
        total += nums[i] - target
        temp.append(total)

    for i in range(k - 1, len(nums)):
        total += nums[i] - target
        if temp[i + 1 - k] < curr_min:
            curr_min = temp[i + 1 - k]
        if total - curr_min >= 0:
            return True
        temp.append(total)

    return False


