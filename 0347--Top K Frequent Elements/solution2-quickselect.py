class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict1 = {}
        for i in range(len(nums)):
            dict1[nums[i]] = dict1.get(nums[i], 0) + 1

        li = list(dict1.keys())
        k = len(li) - k + 1
        start = quick_select(li, 0, len(li) - 1, dict1, k)
        return li[start:]


def partition(li, left, right, dict1):
    # swap the first one with a random element in the list
    rand_id = random.randrange(left, right + 1)
    li[left], li[rand_id] = li[rand_id], li[left]
    i = left
    j = right
    temp = li[left]

    while i < j:
        while i < j and dict1[li[j]] >= dict1[temp]:
            j -= 1
        li[i] = li[j]

        while i < j and dict1[li[i]] <= dict1[temp]:
            i += 1
        li[j] = li[i]

    li[i] = temp

    return i


def quick_select(li, left, right, dict1, k):
    if left < right:
        mid = partition(li, left, right, dict1)
        if k <= (mid - left + 1):
            return quick_select(li, left, mid, dict1, k)
        else:
            return quick_select(li, mid + 1, right, dict1, k - (mid - left + 1))
    else:
        if k == 1:
            return left