class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dict1 = {'6': '9', '9': '6', '0': '0', '1': '1', '8': '8'}

        result = []

        def helper(pos, curr, n):
            if pos >= n // 2:
                if n % 2 == 0:
                    result.append(''.join(list(curr)))
                else:
                    for key in dict1.keys():
                        if key == '6' or key == '9':
                            continue
                        curr[n // 2] = key
                        result.append(''.join(list(curr)))
                return

            for key in dict1.keys():
                if pos == 0 and key == '0':
                    continue
                curr[pos] = key
                curr[n - 1 - pos] = dict1[key]
                helper(pos + 1, curr, n)

        curr = [None] * n
        helper(0, curr, n)

        return result


