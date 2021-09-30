class Solution(object):

    def __init__(self, rects):
        """
        :type rects: List[List[int]]
        """
        self.rects = rects

        prefix = [0]
        for rect in rects:
            area = (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1)
            prefix.append(prefix[-1] + area)

        self.prefix = prefix

    def pick(self):
        """
        :rtype: List[int]
        """
        total = self.prefix[-1]

        rand = random.randrange(0, total + 1)

        left = 1
        right = len(self.prefix) - 1

        while left < right:
            mid = (left + right) // 2
            if rand < self.prefix[mid]:
                right = mid
            else:
                left = mid + 1

        if rand <= self.prefix[left]:
            pos = left - 1
        else:
            pos = left - 2

        rect = self.rects[pos]
        x = random.randrange(rect[0], rect[2] + 1)
        y = random.randrange(rect[1], rect[3] + 1)

        return [x, y]

# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()