# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        if root is None:
            return 0

        parent_value = {root: []}

        queue = [root]
        result = 0

        while len(queue) != 0:
            node = queue.pop(0)
            temp = parent_value[node]
            for i in range(len(temp)):
                temp[i] += node.val
                if temp[i] == targetSum:
                    result += 1

            temp.append(node.val)

            if node.val == targetSum:
                result += 1

            if node.left:
                queue.append(node.left)
                parent_value[node.left] = [i for i in temp]
            if node.right:
                queue.append(node.right)
                parent_value[node.right] = [i for i in temp]

        return result
