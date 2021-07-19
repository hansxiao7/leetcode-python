class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(k):
            result.append(points[i])

        # build the heap
        for j in range((k - 2) // 2, -1, -1):
            sift(result, j, k - 1)

        for m in range(k, len(points)):
            if compare(points[m], result[0]) == -1:
                result[0] = points[m]
                sift(result, 0, k - 1)

        return result


def compare(a, b):
    if (a[0] ** 2 + a[1] ** 2) < (b[0] ** 2 + b[1] ** 2):
        return -1
    else:
        return 1


def sift(li, low, high):
    i = low
    j = 2 * i + 1

    while j <= high:
        if j + 1 <= high and compare(li[j], li[j + 1]) == -1:
            j = j + 1
        if compare(li[i], li[j]) == -1:
            li[i], li[j] = li[j], li[i]
            i = j
            j = 2 * i + 1
        else:
            break