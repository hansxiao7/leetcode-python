class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        set1 = set()
        for i in range(10):
            set1.add(str(i))

        result = ''
        flag = None

        for i in range(len(s)):
            if s[i] not in set1:
                if result == '':
                    if s[i] == ' ' and flag == None:
                        continue
                    elif s[i] == '+' and flag == None:
                        flag = 1
                    elif s[i] == '-' and flag == None:
                        flag = -1
                    else:
                        return 0
                else:
                    break
            else:
                result = result + s[i]
        if result == '':
            return 0
        if flag is None:
            flag = 1

        result = int(result) * flag

        if result < -2 ** 31:
            result = -2 ** 31
        if result > 2 ** 31 - 1:
            result = 2 ** 31 - 1

        return result



