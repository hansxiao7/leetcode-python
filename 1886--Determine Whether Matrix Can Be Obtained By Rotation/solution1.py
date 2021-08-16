class Solution(object):
    def findRotation(self, mat, target):
        """
        :type mat: List[List[int]]
        :type target: List[List[int]]
        :rtype: bool
        """
        m = len(mat)
        n = len(mat[0])

        for k in range(4):
            for i in range(m):
                for j in range(i + 1, n):
                    mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

            for i in range(m):
                mat[i] = mat[i][::-1]

            flag = True
            for i in range(m):
                for j in range(n):
                    if mat[i][j] != target[i][j]:
                        flag = False
                        break

            if flag:
                return True
        return False