"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution(object):
    def cloneTree(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root is None:
            return None
        dict1 = {}

        # create new nodes
        queue = [root]
        while len(queue) != 0:
            node = queue.pop(0)
            if node not in dict1:
                new_node = Node(val=node.val)
                dict1[node] = new_node
            else:
                new_node = dict1[node]

            for i in range(len(node.children)):
                child = node.children[i]
                if child not in dict1:
                    new_child = Node(val=child.val)
                    dict1[node.children[i]] = new_child
                else:
                    new_child = dict1[node.children[i]]

                new_node.children.append(new_child)

                queue.append(node.children[i])

        return dict1[root]

