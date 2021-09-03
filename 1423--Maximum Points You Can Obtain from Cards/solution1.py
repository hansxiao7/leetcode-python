class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        res = 0

        prefix = [0]

        for card in cardPoints:
            prefix.append(prefix[-1] + card)

        left = 0
        right = len(prefix) - 1 - k
        total = prefix[-1]

        while right < len(prefix):
            res = max(res, total - (prefix[right] - prefix[left]))
            left += 1
            right += 1

        return res