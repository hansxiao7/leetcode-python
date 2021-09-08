class Solution(object):
    def minOperations(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: int
        """
        maps = {}
        for i in range(len(target)):
            maps[target[i]] = i

        temp = []
        for num in arr:
            if num in maps:
                temp.append(maps[num])

        if len(temp) == 0:
            return len(target)

        res = [temp[0]]
        for i in range(1, len(temp)):
            if temp[i] > res[-1]:
                res.append(temp[i])
            else:
                # binary search
                tar = temp[i]
                left = 0
                right = len(res) - 1
                while left < right:
                    mid = (left + right) // 2
                    if res[mid] > tar:
                        right = mid
                    elif res[mid] < tar:
                        left = mid + 1
                    else:
                        left = mid
                        break

                if res[left] < tar:
                    left += 1
                res[left] = tar
        return len(target) - len(res)