# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        graph = {}

        def graph_builder(node):
            if node is None:
                return

            if node.left:
                if graph.get(node.val) is None:
                    graph[node.val] = []
                graph[node.val].append(node.left.val)

                if graph.get(node.left.val) is None:
                    graph[node.left.val] = []
                graph[node.left.val].append(node.val)

                graph_builder(node.left)

            if node.right:
                if graph.get(node.val) is None:
                    graph[node.val] = []
                graph[node.val].append(node.right.val)

                if graph.get(node.right.val) is None:
                    graph[node.right.val] = []
                graph[node.right.val].append(node.val)

                graph_builder(node.right)

        graph_builder(root)

        # use BFS to find the values
        visited = set()

        queue = [target.val]
        dis = 0
        result = []

        while len(queue) != 0:
            n_q = len(queue)

            for i in range(n_q):
                node = queue.pop(0)

                if node in visited:
                    continue

                visited.add(node)

                if dis == k:
                    result.append(node)

                children = graph.get(node, [])
                for j in range(len(children)):
                    child = children[j]

                    if child not in visited:
                        queue.append(child)

            dis += 1
            if dis > k:
                break

        return result