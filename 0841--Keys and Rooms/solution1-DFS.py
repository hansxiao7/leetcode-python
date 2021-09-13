class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = set()
        visited.add(0)
        self.res = False

        def helper(pos):
            if len(visited) == len(rooms):
                self.res = True
                return

            for i in range(len(rooms[pos])):
                if rooms[pos][i] not in visited:
                    visited.add(rooms[pos][i])
                    helper(rooms[pos][i])

        helper(0)
        return self.res