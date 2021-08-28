class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        temp = preorder.split(',')

        slot = 1
        for i in temp:
            slot -= 1
            if slot < 0:
                return False
            if i.isnumeric():
                slot += 2

        if slot != 0:
            return False

        return True