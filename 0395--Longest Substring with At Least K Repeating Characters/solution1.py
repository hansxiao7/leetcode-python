class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        result = 0

        for i in range(1, 27):
            left = 0
            counts = {}
            n = 0
            n_c = 0

            for right in range(len(s)):
                if counts.get(s[right], 0) == 0:
                    n_c += 1
                counts[s[right]] = counts.get(s[right], 0) + 1

                if counts[s[right]] == k:
                    n += 1

                while n_c > i:
                    if counts[s[left]] == k:
                        n -= 1
                    counts[s[left]] -= 1
                    if counts[s[left]] == 0:
                        n_c -= 1
                    left += 1

                if n == i:
                    result = max(result, right - left + 1)

        return result


