class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            s_dict = get_dict(s)
            t_dict = get_dict(t)

            s_keys = s_dict.keys()
            for i in range(len(s_keys)):
                if s_dict.get(s_keys[i]) != t_dict.get(s_keys[i]):
                    return False

        else:
            return False

        return True


def get_dict(s):
    result = {}
    for i in s:
        if result.get(i) is None:
            result[i] = 1
        else:
            result[i] += 1

    return result