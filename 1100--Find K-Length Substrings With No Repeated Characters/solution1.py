class Solution(object):
    def numKLenSubstrNoRepeats(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        counts = {}

        left = 0
        result = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1

            while left < right and (max(counts.values()) > 1 or right - left + 1 > k):
                counts[s[left]] -= 1
                left += 1

            if right - left + 1 == k:
                result += 1

        return result

