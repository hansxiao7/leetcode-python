class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dict1 = {}

        left = 0
        result = 0

        for right in range(len(s)):
            dict1[s[right]] = dict1.get(s[right], 0) + 1

            while right - left + 1 - max(dict1.values()) > k:
                dict1[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result