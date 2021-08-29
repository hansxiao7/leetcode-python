# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        graph = {}
        isLeaf = {}

        def buildGraph(node):
            if node is None:
                return

            if node.val not in graph:
                graph[node.val] = []

            if node.left is None and node.right is None:
                isLeaf[node.val] = True
            else:
                isLeaf[node.val] = False

            if node.left:
                if node.left.val not in graph:
                    graph[node.left.val] = []
                graph[node.left.val].append(node.val)
                graph[node.val].append(node.left.val)

                buildGraph(node.left)

            if node.right:
                if node.right.val not in graph:
                    graph[node.right.val] = []
                graph[node.right.val].append(node.val)
                graph[node.val].append(node.right.val)

                buildGraph(node.right)

        buildGraph(root)
        # bfs
        visited = set()
        visited.add(k)
        queue = [k]

        while len(queue) != 0:
            node = queue.pop(0)

            if isLeaf[node]:
                return node

            children = graph.get(node, [])

            for child in children:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)

