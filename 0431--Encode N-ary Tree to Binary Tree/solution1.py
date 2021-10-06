"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Codec:
    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        :type root: Node
        :rtype: TreeNode
        """
        if root is None:
            return None

        node = TreeNode(root.val)

        def helper(arr):
            if arr is None or len(arr) == 0:
                return None

            dummy = TreeNode(0)
            node = dummy
            for i in range(len(arr)):
                node.left = TreeNode(arr[i].val)
                node.left.right = helper(arr[i].children)
                node = node.left

            return dummy.left

        node.left = helper(root.children)
        return node

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        :type data: TreeNode
        :rtype: Node
        """
        if data is None:
            return None

        node = Node(val=data.val)

        def helper(node):
            if node is None:
                return []

            res = []

            while node:
                temp = Node(val=node.val)
                temp.children = helper(node.right)
                res.append(temp)
                node = node.left

            return res

        node.children = helper(data.left)

        return node

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))