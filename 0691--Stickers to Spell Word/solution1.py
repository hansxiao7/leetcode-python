class Solution(object):
    def minStickers(self, stickers, target):
        """
        :type stickers: List[str]
        :type target: str
        :rtype: int
        """
        # build a dict
        dict1 = []

        for sticker in stickers:
            temp = [0 for _ in range(26)]
            for s in sticker:
                temp[ord(s) - ord('a')] += 1

            dict1.append(temp)

        # dfs
        cache = {'': 0}

        def helper(target):
            if target in cache:
                return cache[target]
            if target == '':
                return 0

            target_li = [0 for _ in range(26)]
            for s in target:
                target_li[ord(s) - ord('a')] += 1

            result = sys.maxint
            for i in range(len(stickers)):
                temp = ''
                for j in range(26):
                    if target_li[j] == 0:
                        continue

                    if dict1[i][j] <= target_li[j]:
                        temp += (target_li[j] - dict1[i][j]) * chr(j + ord('a'))

                if len(temp) < len(target):
                    result = min(result, 1 + helper(temp))
                else:
                    continue
            cache[target] = result
            return result

        result = helper(target)
        if result == sys.maxint:
            return -1
        return result