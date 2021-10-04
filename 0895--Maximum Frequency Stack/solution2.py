class FreqStack(object):

    def __init__(self):
        self.counts = {}
        self.freqToVal = {}
        self.maxFreq = 0

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.counts[val] = self.counts.get(val, 0) + 1
        freq = self.counts[val]
        if freq not in self.freqToVal:
            self.freqToVal[freq] = []
        self.freqToVal[freq].append(val)
        self.maxFreq = max(self.maxFreq, freq)

    def pop(self):
        """
        :rtype: int
        """

        res = self.freqToVal[self.maxFreq].pop()
        self.counts[res] -= 1
        if len(self.freqToVal[self.maxFreq]) == 0:
            self.maxFreq -= 1

        return res

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()