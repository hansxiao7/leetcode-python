class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        visited = set()
        self.result = 0

        def helper(row, n):
            if row == n:
                self.result += 1
                return

            for i in range(n):
                flag = 0

                for j in range(1, row + 1):
                    if (row - j, i - j) in visited or (row - j, i + j) in visited or (row - j, i) in visited:
                        flag = 1

                if flag == 1:
                    continue

                visited.add((row, i))
                helper(row + 1, n)
                visited.remove((row, i))

        helper(0, n)

        return self.result