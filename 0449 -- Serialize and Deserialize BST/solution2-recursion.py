# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        result = []
        preorder(result, root)
        result = '[' + ','.join(result) + ']'

        return result

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data[1:-1]
        if data == '':
            return None
        data = data.split(',')
        print(data)
        return helper(data, -sys.maxint, sys.maxint)


def preorder(result, node):
    if node:
        result.append(str(node.val))
        preorder(result, node.left)
        preorder(result, node.right)


def helper(li, min_val, max_val):
    if li == [] or int(li[0]) > max_val or int(li[0]) < min_val:
        return None

    val = int(li.pop(0))
    node = TreeNode(val=val)
    node.left = helper(li, min_val, val)
    node.right = helper(li, val, max_val)

    return node

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans