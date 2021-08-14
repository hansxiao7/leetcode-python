class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.key = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.maps = {}
        self.count = 0
        self.capacity = capacity
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.maps.get(key) is None:
            return -1

        node = self.maps[key]

        # disconnect the node
        node.next.prev = node.prev
        node.prev.next = node.next

        # put it at the head
        temp = self.head.next
        temp.prev = node
        node.next = temp

        node.prev = self.head
        self.head.next = node

        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.maps.get(key) is not None:
            self.maps[key].val = value
            node = self.maps[key]
            node.next.prev = node.prev
            node.prev.next = node.next
        else:
            node = Node(value)
            node.key = key
            self.maps[key] = node
            self.count += 1

        # put it at the head
        temp = self.head.next
        temp.prev = node
        node.next = temp

        node.prev = self.head
        self.head.next = node

        # delete node
        if self.count > self.capacity:
            temp = self.tail.prev.key
            self.maps[temp] = None

            temp_node = self.tail.prev.prev
            self.tail.prev = temp_node
            temp_node.next = self.tail

            self.count -= 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)