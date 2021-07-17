class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        left = 0
        right = m * n - 1
        return binary_search(matrix, target, left, right)


def binary_search(matrix, target, left, right):
    m = len(matrix)
    n = len(matrix[0])
    left_value = matrix[left // n][left % n]
    right_value = matrix[right // n][right % n]
    if left < right:
        mid = (left + right) // 2
        mid_value = matrix[mid // n][mid % n]

        if target < mid_value:
            return binary_search(matrix, target, left, mid)
        elif target > mid_value:
            return binary_search(matrix, target, mid + 1, right)
        else:
            return True
    else:
        if target == left_value:
            return True
        else:
            return False
    return False

