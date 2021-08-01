class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {}
        left = 0
        right = 0
        result = 0

        while left <= right and right < len(s):
            if dict1.get(s[right], -1) == -1:
                result = max(result, right - left + 1)
                dict1[s[right]] = right
                right += 1
            elif dict1[s[right]] != -1:
                dict1[s[left]] = -1
                left += 1

        return result