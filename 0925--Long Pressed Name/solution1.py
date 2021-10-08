class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if len(typed) < len(name):
            return False

        pos1 = 0
        pos2 = 0

        while pos1 < len(name) and pos2 < len(typed):
            c = name[pos1]
            count = 1
            while pos1 < len(name) - 1 and name[pos1 + 1] == c:
                count += 1
                pos1 += 1

            c2 = typed[pos2]
            count2 = 1
            while pos2 < len(typed) - 1 and typed[pos2 + 1] == c2:
                count2 += 1
                pos2 += 1

            if count2 >= count and c == c2:
                pos1 += 1
                pos2 += 1
            else:
                return False

        if pos1 == len(name) and pos2 == len(typed):
            return True
        return False