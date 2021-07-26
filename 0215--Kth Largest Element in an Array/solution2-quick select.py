class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # heap sort
        # quick select
        return quick_select(nums, 0, len(nums) - 1, k)


def partition(li, left, right):
    # randomly swap the 1st element with others
    rand_id = random.randrange(left, right + 1)
    li[left], li[rand_id] = li[rand_id], li[left]

    i = left
    j = right
    temp = li[left]

    while i < j:
        while i < j and li[j] <= temp:
            j -= 1
        li[i] = li[j]

        while i < j and li[i] > temp:
            i += 1
        li[j] = li[i]

    li[i] = temp

    return i


def quick_select(nums, left, right, k):
    if left < right:
        mid = partition(nums, left, right)
        if (mid - left + 1) >= k:
            result = quick_select(nums, left, mid, k)
        else:
            result = quick_select(nums, mid + 1, right, k - (mid - left + 1))
    else:
        return nums[left]

    return result

