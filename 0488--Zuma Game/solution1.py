class Solution(object):
    def findMinStep(self, board, hand):
        """
        :type board: str
        :type hand: str
        :rtype: int
        """

        def check(s):
            pos = 0
            while pos < len(s):
                c = s[pos]
                start = pos
                count = 1
                while pos + 1 < len(s) and s[pos + 1] == c:
                    count += 1
                    pos += 1

                if count >= 3:
                    return check(s[:start] + s[pos + 1:])

                pos += 1
            return s

        cache = {}

        def helper(s, hand):
            if (s, hand) in cache:
                return cache[(s, hand)]
            s = check(s)
            if s == '':
                return 0

            res = sys.maxint
            for i in range(len(s)):
                for j in range(len(hand)):
                    left = hand[:j]
                    right = hand[j + 1:]
                    res = min(res, 1 + helper(s[:i + 1] + hand[j] + s[i + 1:], left + right))
                    hand = left + hand[j] + right

            cache[(s, hand)] = res
            return res

        res = helper(board, hand)
        if res == sys.maxint:
            return -1
        return res