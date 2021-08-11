class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        nums = {}

        for i in range(len(arr)):
            nums[arr[i]] = nums.get(arr[i], 0) + 1

        arr.sort(key=abs)
        for i in range(len(arr)):
            if nums[arr[i]] == 0:
                continue
            if nums.get(2 * arr[i], 0) > 0:
                nums[2 * arr[i]] -= 1
                nums[arr[i]] -= 1
                continue
            else:
                return False

        return True