class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.maps = {}
        self.arr = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.arr.append(val)
        if val not in self.maps or self.maps[val] is None:
            self.maps[val] = len(self.arr) - 1
            return True
        else:
            return False

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.maps or self.maps[val] is None:
            return False

        pos = self.maps[val]
        if pos == len(self.arr) - 1:
            self.arr.pop()
            self.maps[val] = None
            return True

        newVal = self.arr.pop()

        self.maps[newVal] = pos
        self.arr[pos] = newVal
        self.maps[val] = None

        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        randID = random.randrange(len(self.arr))
        return self.arr[randID]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()