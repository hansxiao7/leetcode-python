class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        target = {}

        for c in t:
            target[c] = target.get(c, 0) + 1

        maps = {}
        result = ''

        left = 0
        count = 0

        for right in range(len(s)):
            if s[right] in target:
                if len(maps.keys()) == 0:
                    left = right
                maps[s[right]] = maps.get(s[right], 0) + 1
                if maps[s[right]] == target[s[right]]:
                    count += 1

            while left < right and (s[left] not in target or maps.get(s[left], 0) > target.get(s[left])):
                if s[left] in maps:
                    maps[s[left]] -= 1
                left += 1

            if count == len(target.keys()):
                if result == '' or right - left + 1 < len(result):
                    result = s[left: right + 1]

        return result