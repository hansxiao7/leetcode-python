class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        visited = set()

        def helper(row, curr, n):
            if row == n:
                result.append(list(curr))
                return

            for i in range(n):
                flag = 0

                for j in range(1, row + 1):
                    if (row - j, i - j) in visited or (row - j, i + j) in visited or (row - j, i) in visited:
                        flag = 1
                        break

                if flag == 1:
                    continue

                temp = '.' * i + 'Q' + '.' * (n - i - 1)
                curr.append(temp)
                visited.add((row, i))
                helper(row + 1, curr, n)
                visited.remove((row, i))
                curr.pop()

        helper(0, [], n)

        return result


