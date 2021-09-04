class LockingTree(object):

    def __init__(self, parent):
        """
        :type parent: List[int]
        """
        self.children = {}

        for i in range(len(parent)):
            if parent[i] not in self.children:
                self.children[parent[i]] = []

            self.children[parent[i]].append(i)

        self.locked = {}
        self.parents = parent

    def lock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """

        if num not in self.locked:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """

        if num in self.locked:
            if self.locked[num] == user:
                self.locked.pop(num)
                return True
            else:
                return False
        return False

    def upgrade(self, num, user):
        """
        :type num: int
        :type user: int
        :rtype: bool
        """
        if num in self.locked:
            return False

        locked_children = []
        queue = list(self.children.get(num, []))
        # bfs
        while len(queue) != 0:
            node = queue.pop(0)

            if node in self.locked:
                locked_children.append(node)

            temp = self.children.get(node, [])

            for i in range(len(temp)):
                queue.append(temp[i])

        if len(locked_children) == 0:
            return False

        pos = self.parents[num]
        while pos >= 0:
            if pos in self.locked:
                return False
            pos = self.parents[pos]

        self.locked[num] = user
        for child in locked_children:
            self.locked.pop(child)

        return True
# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)