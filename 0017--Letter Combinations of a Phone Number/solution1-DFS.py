class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == '':
            return []

        dict1 = {}

        x = ord('a')

        for i in range(2, 10):
            dict1[i] = []

            if i != 7 and i != 9:
                for j in range(3):
                    dict1[i].append(chr(x))
                    x += 1
            else:
                for j in range(4):
                    dict1[i].append(chr(x))
                    x += 1
        return dfs(digits, dict1, 0)


def dfs(d, dict1, pos):
    if pos >= len(d):
        return ['']
    result = []
    for i in range(len(dict1[int(d[pos])])):
        temp2 = dfs(d, dict1, pos + 1)
        for j in range(len(temp2)):
            temp = dict1[int(d[pos])][i]
            temp = temp + temp2[j]
            result.append(temp)

    return result





