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

        maps = {}

        def helper(pos, arr, curr):
            if len(curr) not in maps:
                maps[len(curr)] = set()
            maps[len(curr)].add(sum(curr))

            if pos == len(arr):
                return

            for i in range(pos, len(arr)):
                helper(i + 1, arr, curr + [arr[i]])

        helper(0, nums2, [])

        for key in maps:
            maps[key] = list(maps[key])
            maps[key].sort()

        self.res = abs(sum(nums1) - sum(nums2))
        visited = set()

        def comb(pos, curr):
            x = len(curr)
            currValue = sum(curr)
            if (x, currValue) not in visited:
                visited.add((x, currValue))
                temp = maps[n - x]

                left = 0
                right = len(temp) - 1
                target = (total - 2 * currValue) / 2.0
                while left < right:
                    mid = (left + right) // 2
                    if temp[mid] < target:
                        left = mid + 1
                    elif temp[mid] > target:
                        right = mid
                    else:
                        left = mid
                        break
                self.res = min(self.res, abs(total - 2 * (currValue + temp[left])))

                if temp[left] > target and left != 0:
                    self.res = min(self.res, abs(total - 2 * (currValue + temp[left - 1])))

                if temp[left] < target and left != len(temp) - 1:
                    self.res = min(self.res, abs(total - 2 * (currValue + temp[left + 1])))

            if pos == len(nums1):
                return

            for i in range(pos, len(nums1)):
                comb(i + 1, curr + [nums1[i]])

        comb(0, [])

        return self.res