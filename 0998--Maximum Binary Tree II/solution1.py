# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        nodeList = []

        def inorder(node):
            if node:
                inorder(node.left)
                nodeList.append(node.val)
                inorder(node.right)

        inorder(root)
        nodeList.append(val)

        stack = []
        left = [-1 for _ in range(len(nodeList))]

        for i in range(len(nodeList)):
            while len(stack) != 0 and nodeList[i] > nodeList[stack[-1]]:
                stack.pop()

            if len(stack) != 0:
                left[i] = stack[-1]

            stack.append(i)

        stack = []
        right = [-1 for _ in range(len(nodeList))]

        for i in range(len(nodeList) - 1, -1, -1):
            while len(stack) != 0 and nodeList[i] > nodeList[stack[-1]]:
                stack.pop()

            if len(stack) != 0:
                right[i] = stack[-1]

            stack.append(i)

        nodes = []
        for i in range(len(nodeList)):
            nodes.append(TreeNode(val=nodeList[i]))

        for i in range(len(nodeList)):
            if left[i] == -1 and right[i] == -1:
                root = nodes[i]
            elif left[i] != -1 and right[i] != -1:
                if nodeList[left[i]] < nodeList[right[i]]:
                    nodes[left[i]].right = nodes[i]
                else:
                    nodes[right[i]].left = nodes[i]
            elif left[i] != -1 and right[i] == -1:
                nodes[left[i]].right = nodes[i]
            elif left[i] == -1 and right[i] != -1:
                nodes[right[i]].left = nodes[i]

        return root
