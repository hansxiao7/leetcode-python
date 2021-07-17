class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # Find row
        row = find_row(matrix, target, 0, len(matrix) - 1)
        if row is None:
            return False
        result = binary_search(matrix[row], target, 0, len(matrix[row]) - 1)
        if result is None:
            return False
        else:
            return True


def binary_search(li, target, left, right):
    if left < right:
        mid = (left + right) // 2
        if target < li[mid]:
            return binary_search(li, target, left, mid)
        elif target > li[mid]:
            return binary_search(li, target, mid + 1, right)
        elif target == li[mid]:
            return mid
    else:
        if target == li[left]:
            return left
        else:
            return None


def find_row(matrix, target, left, right):
    if left < right - 1:
        mid = (left + right) // 2
        if target < matrix[mid][0]:
            return find_row(matrix, target, left, mid - 1)
        elif target > matrix[mid][0]:
            return find_row(matrix, target, mid, right)
        else:
            return mid
    elif left == right - 1:
        if target >= matrix[left][0] and target < matrix[right][0]:
            return left
        elif target >= matrix[right][0]:
            return right
    else:
        if target >= matrix[left][0]:
            return left
        else:
            return None



