class Solution(object):
    def maximumNumber(self, num, change):
        """
        :type num: str
        :type change: List[int]
        :rtype: str
        """
        # 1. brute force
        # 2. sliding window
        flag = False
        result = list(num)
        for i in range(len(num)):
            n = int(num[i])
            if n < change[n]:
                result[i] = str(change[n])
                flag = True
            elif n == change[n] and flag:
                continue
            else:
                if flag:
                    break

        return ''.join(result)

