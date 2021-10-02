class Solution(object):
    def possibleBipartition(self, n, dislikes):
        """
        :type n: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        maps = {}
        for x, y in dislikes:
            if x not in maps:
                maps[x] = []
            if y not in maps:
                maps[y] = []
            maps[x].append(y)
            maps[y].append(x)

        colors = [-1] * (n + 1)

        for i in range(1, n + 1):
            queue = [i]

            while len(queue) != 0:
                node = queue.pop(0)

                if colors[node] == -1:
                    colors[node] = 1

                if colors[node] == 1:
                    flag = 2
                else:
                    flag = 1

                children = maps.get(node, [])

                for i in range(len(children)):
                    child = children[i]
                    if colors[child] == -1:
                        colors[child] = flag
                        queue.append(child)
                    elif colors[child] == flag:
                        continue
                    else:
                        return False
        return True