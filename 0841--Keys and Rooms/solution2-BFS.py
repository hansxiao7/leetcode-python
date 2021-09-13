class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        # BFS
        visited = set()
        visited.add(0)
        queue = collections.deque()

        queue.append(0)

        while len(queue) != 0:
            node = queue.popleft()

            keys = rooms[node]
            for key in keys:
                if key not in visited:
                    visited.add(key)
                    queue.append(key)

        if len(visited) == len(rooms):
            return True
        return False