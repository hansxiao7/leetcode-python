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

        # bidirectional BFS
        s1 = set()
        s2 = set()
        s1.add(0)
        s2.add(len(arr) - 1)

        visited = set()
        rank = 0

        while len(s1) != 0 and len(s2) != 0:
            if len(s2) < len(s1):
                s1, s2 = s2, s1

            s = set()

            for node in s1:
                if node in s2:
                    return rank

                visited.add(node)
                children = maps.get(arr[node], [])

                for i in range(len(children)):
                    child = children[i]

                    if child not in visited:
                        s.add(child)

                left = node - 1
                right = node + 1

                if left >= 0 and left not in visited:
                    s.add(left)

                if right < len(arr) and right not in visited:
                    s.add(right)

            rank += 1
            s1 = s