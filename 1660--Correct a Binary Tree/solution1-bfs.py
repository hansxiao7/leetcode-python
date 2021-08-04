# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def correctBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        queue = [root]
        path = {}
        result = None

        while len(queue) != 0:
            n = len(queue)
            visited = set()
            for i in range(n):
                node = queue.pop(0)
                if node.right in visited:
                    result = node
                    break
                visited.add(node)

                if node.right:
                    path[node.right] = [node, 1]
                    queue.append(node.right)

                if node.left:
                    path[node.left] = [node, 0]
                    queue.append(node.left)

        parent, pos = path[result]
        if pos == 0:
            parent.left = None
        else:
            parent.right = None

        return root