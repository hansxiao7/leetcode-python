"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if node is None:
            return None

        root = node
        queue = [node]
        new_root = Node(val=node.val)

        maps = {node: new_root}
        visited = set()

        while len(queue) != 0:
            node = queue.pop(0)

            visited.add(node)

            children = node.neighbors

            for i in range(len(children)):
                child = children[i]
                if child not in visited:
                    new_child = Node(val=child.val)
                    maps[child] = new_child

                    queue.append(child)
        # 连接
        for key in maps.keys():
            children = key.neighbors
            for i in range(len(children)):
                child = children[i]
                maps[key].neighbors.append(maps[child])

        return maps[root]