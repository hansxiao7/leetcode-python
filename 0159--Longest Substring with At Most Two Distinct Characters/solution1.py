class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """

        dict1 = {}
        result = 0
        n = 0
        left = 0

        for right in range(len(s)):
            if dict1.get(s[right], 0) == 0:
                n += 1

            dict1[s[right]] = dict1.get(s[right], 0) + 1

            while n > 2:
                dict1[s[left]] -= 1
                if dict1[s[left]] == 0:
                    n -= 1
                left += 1

            result = max(result, right - left + 1)

        return result