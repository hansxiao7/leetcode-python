class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        pow = 10

        int1 = 0

        for i in range(len(num1)):
            int1 = int1 * pow + ord(num1[i]) - ord('0')

        int2 = 0

        for i in range(len(num2)):
            int2 = int2 * pow + ord(num2[i]) - ord('0')

        return str(int1 * int2)