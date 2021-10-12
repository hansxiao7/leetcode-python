class Solution(object):
    def minimumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) // 2
        total = sum(nums)
        nums1 = nums[:n]
        nums2 = nums[n:]

        maps = {0: [0]}

        def helper(pos, arr, curr, k):
            if k == 0:
                if len(curr) not in maps:
                    maps[len(curr)] = []
                maps[len(curr)].append(sum(curr))
                return

            for i in range(pos, len(arr)):
                helper(i + 1, arr, curr + [arr[i]], k - 1)

        for i in range(1, n + 1):
            helper(0, nums2, [], i)

        for key in maps:
            maps[key].sort()

        self.res = abs(sum(nums1) - sum(nums2))
        visited = set()

        def comb(pos, x, k, curr):
            if k == 0:
                if (x, curr) in visited:
                    return
                temp = maps[n - x]

                visited.add((x, curr))
                left = 0
                right = len(temp) - 1
                target = (total - 2 * curr) / 2.0
                while left < right:
                    mid = (left + right) // 2
                    if temp[mid] < target:
                        left = mid + 1
                    elif temp[mid] > target:
                        right = mid
                    else:
                        left = mid
                        break
                self.res = min(self.res, abs(total - 2 * (curr + temp[left])))

                if temp[left] > target and left != 0:
                    self.res = min(self.res, abs(total - 2 * (curr + temp[left - 1])))

                if temp[left] < target and left != len(temp) - 1:
                    self.res = min(self.res, abs(total - 2 * (curr + temp[left + 1])))
                return

            for i in range(pos, len(nums1)):
                comb(i + 1, x, k - 1, curr + nums1[i])

        for i in range(1, n + 1):
            comb(0, i, i, 0)

        return self.res