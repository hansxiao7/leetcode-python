class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        m = len(mat)
        n = len(mat[0])

        minV = sys.maxint
        for i in range(m):
            minV = min(minV, min(mat[i]))

        if minV > threshold:
            return 0

        left = 1
        right = min(m, n)

        # prefix sum
        prefix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + mat[i - 1][j - 1]

        for i in range(m):
            temp = [0]
            total = 0
            for j in range(n):
                total += mat[i][j]
                temp.append(total)
            prefix.append(temp)

        def check_val(val, threshold):
            m = len(mat)
            n = len(mat[0])

            flag = False

            for i in range(val, m + 1):
                for j in range(val, n + 1):
                    sumV = prefix[i][j] - prefix[i - val][j] - prefix[i][j - val] + prefix[i - val][j - val]

                    if sumV <= threshold:
                        # val is too small
                        return True
            # val is too large
            return False

        while left < right:
            mid = (left + right) // 2
            if check_val(mid, threshold):
                left = mid + 1
            else:
                right = mid
        if check_val(left, threshold) is False:
            return left - 1
        return left