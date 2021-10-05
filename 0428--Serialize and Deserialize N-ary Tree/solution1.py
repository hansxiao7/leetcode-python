"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: Node
        :rtype: str
        """

        def helper(node):
            if node is None:
                return ''
            children = node.children
            temp = ''
            if children is not None:
                for i in range(len(children)):
                    temp += '(' + helper(children[i]) + ')'

            return str(node.val) + temp

        res = helper(root)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: Node
        """

        def helper(s):
            if s == '':
                return None

            val = ''
            pos = 0

            while pos < len(s) and s[pos] != '(':
                val = val + s[pos]
                pos += 1

            node = Node(val=int(val))
            node.children = []

            while pos < len(s):
                bal = 0
                start = pos
                end = pos

                while (end < len(s) and bal != 0) or start == end:
                    if s[end] == '(':
                        bal += 1
                    elif s[end] == ')':
                        bal -= 1

                    end += 1

                node.children.append(helper(s[start + 1: end - 1]))
                pos = end

            return node

        return helper(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))