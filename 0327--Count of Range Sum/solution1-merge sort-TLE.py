class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)

        # merget sort
        def merge_sort(left, right):
            if left < right:
                mid = (left + right) // 2
                l = merge_sort(left, mid)
                r = merge_sort(mid + 1, right)

                m = merge(left, mid, right)
                return l + r + m
            else:
                return 0

        def merge(left, mid, right):
            temp = [0] * len(prefix)
            i = left
            j = mid + 1
            k = left

            # calculate merge result
            l = i
            r2 = j
            r1 = j

            result = 0
            while l <= mid:
                while r1 <= right and prefix[r1] - prefix[l] < lower:
                    r1 += 1

                while r2 <= right and prefix[r2] - prefix[l] <= upper:
                    r2 += 1

                result += r2 - r1

                l += 1

            while i <= mid and j <= right:
                if prefix[i] <= prefix[j]:
                    temp[k] = prefix[i]
                    i += 1
                    k += 1
                else:
                    temp[k] = prefix[j]
                    j += 1
                    k += 1

            while i <= mid:
                temp[k] = prefix[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = prefix[j]
                j += 1
                k += 1

            for l in range(left, right + 1):
                prefix[l] = temp[l]

            return result

        res = merge_sort(0, len(prefix) - 1)

        return res