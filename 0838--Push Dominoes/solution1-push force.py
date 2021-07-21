class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """
        L = [0 for i in range(len(dominoes))]
        R = [0 for i in range(len(dominoes))]

        count = 0
        for i in range(len(dominoes)):
            if dominoes[i] == 'R':
                count = 1
            if dominoes[i] == 'L':
                count = 0
            if count == 0:
                continue
            R[i] = count
            count += 1

        count = 0
        for j in range(len(dominoes) - 1, -1, -1):
            if dominoes[j] == 'L':
                count = 1
            if dominoes[j] == 'R':
                count = 0
            if count == 0:
                continue
            L[j] = count
            count += 1

        result = ''
        for k in range(len(dominoes)):
            if L[k] * R[k] == 0:
                if L[k] == R[k] == 0:
                    result += '.'
                elif L[k] == 0:
                    result += 'R'
                else:
                    result += 'L'
            else:
                if L[k] > R[k]:
                    result += 'R'
                elif L[k] < R[k]:
                    result += 'L'
                else:
                    result += '.'

        return result