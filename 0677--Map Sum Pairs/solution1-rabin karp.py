class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # rabin-karp
        self.mod = 10 ** 6
        self.pow = 31
        self.graph = {}
        self.curr_keys = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        dis = 0
        if self.curr_keys.get(key) is None:
            self.curr_keys[key] = val
        else:
            dis = self.curr_keys[key]
            self.curr_keys[key] = val
        temp = 0

        for i in range(len(key)):
            s = key[i]
            temp = (temp * self.pow + ord(s)) % self.mod
            self.graph[temp] = self.graph.get(temp, 0) + val - dis

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        temp = 0
        for i in range(len(prefix)):
            s = prefix[i]
            temp = (temp * self.pow + ord(s)) % self.mod

        return self.graph.get(temp, 0)

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)