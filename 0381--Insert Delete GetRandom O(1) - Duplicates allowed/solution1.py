class RandomizedCollection(object):

    def __init__(self):
        self.count = 0
        self.arr = []
        self.maps = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        flag = True
        if len(self.maps.get(val, set())) == 0:
            self.maps[val] = set()
        else:
            flag = False

        self.maps[val].add(self.count)
        if len(self.arr) > self.count:
            self.arr[self.count] = val
        else:
            self.arr.append(val)

        self.count += 1

        return flag

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if len(self.maps.get(val, set())) == 0:
            return False

        last = self.arr[self.count - 1]

        if last == val:
            self.maps[val].remove(self.count - 1)
        else:
            for i in self.maps[val]:
                pos = i
                break

            self.maps[val].remove(pos)
            self.maps[last].remove(self.count - 1)
            self.maps[last].add(pos)
            self.arr[pos] = last

        self.count -= 1

        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return self.arr[random.randrange(0, self.count)]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()