class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        s1 = []
        s2 = []

        if len(a) < len(b):
            a, b = b, a

        b = '0' * (len(a) - len(b)) + b

        for c in a:
            s1.append(c)

        for c in b:
            s2.append(c)
        prev = 0

        result = ''

        while len(s1) != 0 and len(s2) != 0:
            temp = int(s1.pop()) + int(s2.pop()) + prev
            if temp == 0 or temp == 1:
                result = str(temp) + result
                prev = 0
            elif temp >= 2:
                result = str(temp - 2) + result
                prev = 1

        if prev == 1:
            result = '1' + result

        return result
