class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        temp1 = set()
        for i in range(len(leftChild)):
            temp1.add(leftChild[i])
            temp1.add(rightChild[i])

        head_node = []
        for i in range(n):
            if i not in temp1:
                head_node.append(i)

        if len(head_node) != 1:
            return False

        # BFS
        head = head_node[0]

        queue = [head]
        visited = [0 for _ in range(n)]

        while len(queue) != 0:
            node = queue.pop(0)
            if visited[node] == 1:
                return False
            visited[node] = 1

            if leftChild[node] != -1:
                if visited[leftChild[node]] == 1:
                    return False
                else:
                    queue.append(leftChild[node])

            if rightChild[node] != -1:
                if visited[rightChild[node]] == 1:
                    return False
                else:
                    queue.append(rightChild[node])

        for i in range(n):
            if visited[i] != 1:
                return False
        return True