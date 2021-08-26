class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = [0] * len(nums)

        def merge_sort(left, right):
            if left < right:
                mid = (left + right) // 2

                l = merge_sort(left, mid)
                r = merge_sort(mid + 1, right)

                mid = merge(left, mid, right)

                return l + r + mid
            else:
                return 0

        def merge(left, mid, right):
            result = 0

            i = left
            j = mid + 1

            k = left

            # find results
            pL = left
            pR = mid + 1

            while pL <= mid and pR <= right:
                if nums[pL] <= 2 * nums[pR]:
                    pL += 1
                else:
                    result += mid - pL + 1
                    pR += 1

            while i <= mid and j <= right:
                if nums[i] < nums[j]:
                    temp[k] = nums[i]
                    k += 1
                    i += 1
                else:  # nums[i] >= nums[j]:
                    temp[k] = nums[j]
                    j += 1
                    k += 1

            while i <= mid:
                temp[k] = nums[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = nums[j]
                j += 1
                k += 1
            for l in range(left, right + 1):
                nums[l] = temp[l]

            return result

        return merge_sort(0, len(nums) - 1)