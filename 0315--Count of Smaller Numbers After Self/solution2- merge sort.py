class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # merge sort
        result = [0] * len(nums)

        li = []

        for i in range(len(nums)):
            li.append((nums[i], i))

        def merge_sort(left, right):
            if left < right:
                mid = (left + right) // 2
                merge_sort(left, mid)
                merge_sort(mid + 1, right)

                merge(left, mid, right)

        def merge(left, mid, right):
            temp = [[] for _ in range(len(li))]

            i = left
            j = mid + 1
            k = left

            # update result
            count = 0

            while i <= mid and j <= right:
                if li[i][0] <= li[j][0]:
                    temp[k] = li[i]
                    result[li[i][1]] += count
                    i += 1
                    k += 1

                else:
                    count += 1
                    temp[k] = li[j]
                    j += 1
                    k += 1

            while i <= mid:
                result[li[i][1]] += count
                temp[k] = li[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = li[j]
                j += 1
                k += 1

            for i in range(left, right + 1):
                li[i] = temp[i]

        merge_sort(0, len(nums) - 1)
        return result