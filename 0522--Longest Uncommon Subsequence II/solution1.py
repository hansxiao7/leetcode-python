class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """

        def helper(a, b):
            # check is a is the subsequence of b
            if len(a) > len(b):
                return False
            else:
                while len(a) != 0 and len(b) != 0:
                    if a[-1] != b[-1]:
                        b = b[:len(b) - 1]
                    else:
                        a = a[:len(a) - 1]
                        b = b[:len(b) - 1]

                if len(a) == 0:
                    return True
                else:
                    return False

        result = -1

        for i in range(len(strs)):
            flag = False
            for j in range(len(strs)):
                if i == j:
                    continue

                temp = helper(strs[i], strs[j])
                if temp:
                    flag = True
                    break

            if flag:
                continue
            else:
                result = max(len(strs[i]), result)

        return result
