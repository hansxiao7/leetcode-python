class Solution(object):
    def minAbsDifference(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        cache = {}

        def find_all_sum(pos, li):
            if pos in cache:
                return cache[pos]
            if pos == len(li):
                return set()

            result = set()

            for i in range(pos, len(li)):
                temp = find_all_sum(i + 1, li)
                result.add(li[i])
                for j in temp:
                    result.add(j + li[i])
            cache[pos] = result
            return result

        mid = (len(nums) - 1) // 2
        l = nums[:mid + 1]
        r = nums[mid + 1:]

        l_sum = find_all_sum(0, l)
        l_sum.add(0)

        cache = {}
        r_sum = find_all_sum(0, r)
        r_sum.add(0)
        r_sum = list(r_sum)
        r_sum.sort()

        result = sys.maxint
        for n_l in l_sum:
            target = goal - n_l
            pos = binary_search(r_sum, 0, len(r_sum) - 1, target)
            if r_sum[pos] == target:
                return 0
            else:
                if r_sum[pos] < target:
                    result = min(result, abs(target - r_sum[pos]), abs(target - r_sum[min(pos + 1, len(r_sum) - 1)]))
                else:
                    result = min(result, abs(target - r_sum[pos]), abs(target - r_sum[max(pos - 1, 0)]))
            result = min(result, abs(target))
        return result


def binary_search(li, left, right, target):
    if left < right:
        mid = (left + right) // 2
        if li[mid] < target:
            return binary_search(li, mid + 1, right, target)
        elif li[mid] > target:
            return binary_search(li, left, mid, target)
        else:
            return mid
    else:
        return left
