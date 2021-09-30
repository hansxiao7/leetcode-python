class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        prefix = [0]
        for num in w:
            prefix.append(prefix[-1] + num)

        self.prefix = prefix

    def pickIndex(self):
        """
        :rtype: int
        """
        total = self.prefix[-1]
        rand = random.randrange(1, total + 1)

        # Binary search
        left = 0
        right = len(self.prefix) - 1

        while left < right:
            mid = (left + right) // 2
            if self.prefix[mid] < rand:
                left = mid + 1
            elif self.prefix[mid] > rand:
                right = mid
            else:
                return mid - 1

        return left - 1

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()