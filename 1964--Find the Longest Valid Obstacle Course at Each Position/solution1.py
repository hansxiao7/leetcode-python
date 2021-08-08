class Solution(object):
    def longestObstacleCourseAtEachPosition(self, obstacles):
        """
        :type obstacles: List[int]
        :rtype: List[int]
        """
        result = []

        temp = []

        n = len(obstacles)
        for i in range(n):
            if temp == [] or obstacles[i] >= temp[-1]:
                temp.append(obstacles[i])
                result.append(len(temp))
            else:  # 找到第一个比它大的
                first_id = binary_search(temp, 0, len(temp) - 1, obstacles[i])
                temp[first_id] = obstacles[i]
                result.append(first_id + 1)

        return result


def binary_search(li, left, right, target):
    if left < right:
        mid = (left + right) // 2
        if li[mid] <= target:
            return binary_search(li, mid + 1, right, target)
        else:
            return binary_search(li, left, mid, target)
    else:
        return left
