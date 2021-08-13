class SnapshotArray(object):

    def __init__(self, length):
        """
        :type length: int
        """
        self.array = {}
        self.memory = {}
        self.snap_id = 0

    def set(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.array[index] = val

    def snap(self):
        """
        :rtype: int
        """
        self.memory[self.snap_id] = self.array.copy()
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        """
        :type index: int
        :type snap_id: int
        :rtype: int
        """
        return self.memory[snap_id].get(index, 0)


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)