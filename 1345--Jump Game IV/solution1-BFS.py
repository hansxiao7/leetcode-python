class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        maps = {}

        for i in range(len(arr)):
            if arr[i] not in maps:
                maps[arr[i]] = []

            maps[arr[i]].append(i)

        # BFS
        queue = collections.deque()
        queue.append(0)
        visited = set()
        visited.add(0)
        rank = 0
        while len(queue) != 0:
            n_q = len(queue)
            for i in range(n_q):
                node = queue.popleft()

                if node == len(arr) - 1:
                    return rank

                children = maps.get(arr[node])

                for j in range(len(children)):
                    child = children[j]

                    if child not in visited:
                        visited.add(child)
                        queue.append(child)
                maps[arr[node]] = []
                left = node - 1
                right = node + 1

                if left >= 0 and left not in visited:
                    visited.add(left)
                    queue.append(left)

                if right < len(arr) and right not in visited:
                    visited.add(right)
                    queue.append(right)

            rank += 1


