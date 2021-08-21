class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dict1 = {'6': '9', '9': '6', '0': '0', '1': '1', '8': '8'}

        left = 0
        right = len(num) - 1

        while left <= right:
            if dict1.get(num[left]) == num[right]:
                left += 1
                right -= 1
            else:
                return False

        return True