class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 3:
            return list(set(tuple(nums)))
        result = []

        def three_parts(left, right, n):
            if left < right:
                target = nums[left]

                i = left
                j = left
                k = right

                while j <= k:
                    if nums[j] < target:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                        j += 1
                    elif nums[j] > target:
                        nums[j], nums[k] = nums[k], nums[j]
                        k -= 1
                    else:
                        j += 1

                # left : i 个 right: right - k个
                l = i - left
                r = right - k
                m = right - left + 1 - l - r

                if m > n // 3:
                    result.append(target)

                if l <= n // 3 and r <= n // 3:
                    return
                elif l > n // 3 and r > n // 3:
                    three_parts(left, i - 1, n)
                    three_parts(k + 1, right, n)
                elif l > n // 3 and r <= n // 3:
                    three_parts(left, i - 1, n)
                elif r > n // 3 and l <= n // 3:
                    three_parts(k + 1, right, n)

        three_parts(0, len(nums) - 1, len(nums))
        return result

