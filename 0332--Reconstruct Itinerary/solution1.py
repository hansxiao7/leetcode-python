class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        maps = {}

        for x, y in tickets:
            if x not in maps:
                maps[x] = []
            maps[x].append(y)

        n = len(tickets)
        visited = {}
        for key in maps:
            maps[key].sort()
            visited[key] = [False] * len(maps[key])

        self.res = None

        def helper(currNode, currList):
            if self.res is not None:
                return
            if len(currList) == n + 1 and self.res is None:
                self.res = list(currList)
                return

            children = maps.get(currNode, [])
            if children == []:
                return

            for i in range(len(children)):
                child = children[i]
                if visited[currNode][i] is False:
                    visited[currNode][i] = True
                    helper(child, currList + [child])
                    visited[currNode][i] = False

        helper('JFK', ['JFK'])

        return self.res