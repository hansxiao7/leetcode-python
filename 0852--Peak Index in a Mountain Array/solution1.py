class Solution(object):
    def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        return find_peak(arr, 0, len(arr) - 1)


def find_peak(arr, left, right):
    if left + 1 < right:
        mid = (left + right) // 2
        max_n = max(arr[mid], arr[mid - 1], arr[mid + 1])

        if max_n == arr[mid]:
            return mid
        elif max_n == arr[mid - 1]:
            result = find_peak(arr, left, mid - 1)
        elif max_n == arr[mid + 1]:
            result = find_peak(arr, mid + 1, right)
    elif left + 1 == right:
        if arr[left] > arr[right]:
            return left
        else:
            return right
    else:
        return left

    return result