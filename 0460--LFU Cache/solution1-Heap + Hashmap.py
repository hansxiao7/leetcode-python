class Node:
    def __init__(self, val):
        self.val = val
        self.key = None
        self.tick = None
        self.freq = None


class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.map = {}
        self.heap = []
        self.time = 0
        self.capacity = capacity
        self.curr_capacity = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.map.get(key) is None:
            return -1

        node = self.map[key]
        node.tick = self.time
        node.freq += 1

        for low in range((len(self.heap) - 2) // 2, -1, -1):
            sift(self.heap, low, len(self.heap) - 1)

        self.time += 1
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.map.get(key) is not None:
            node = self.map[key]
            node.val = value
            node.freq += 1
            node.tick = self.time
        else:
            node = Node(value)
            node.key = key
            node.freq = 1
            self.map[key] = node
            node.tick = self.time
            self.heap.append(node)

            self.curr_capacity += 1

            if self.curr_capacity > self.capacity:
                self.map[self.heap[0].key] = None
                self.heap[0] = self.heap[-1]
                self.heap = self.heap[:len(self.heap) - 1]
                self.curr_capacity -= 1

        for low in range((len(self.heap) - 2) // 2, -1, -1):
            sift(self.heap, low, len(self.heap) - 1)

        self.time += 1


def sift(heap, low, high):
    i = low
    j = 2 * i + 1

    while j <= high:
        if j + 1 <= high and compare(heap[j + 1], heap[j]) == -1:
            j = j + 1

        if compare(heap[i], heap[j]) == 1:
            heap[i], heap[j] = heap[j], heap[i]
            i = j
            j = 2 * i + 1
        else:
            break


def compare(n1, n2):
    if n1.freq < n2.freq:
        return -1
    elif n1.freq > n2.freq:
        return 1
    else:
        if n1.tick < n2.tick:
            return -1
        else:
            return 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)