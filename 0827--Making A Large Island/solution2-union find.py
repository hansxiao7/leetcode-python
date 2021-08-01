class Solution(object):
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # union find
        graph = {}
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, i, j, graph, grid)
        result = 0
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 0:
                    roots = set()
                    temp = 0
                    if graph.get((x - 1, y)):
                        root_u, val_u = find(x - 1, y, graph)
                        if root_u not in roots:
                            roots.add(root_u)
                            temp += val_u

                    if graph.get((x + 1, y)):
                        root_d, val_d = find(x + 1, y, graph)
                        if root_d not in roots:
                            roots.add(root_d)
                            temp += val_d

                    if graph.get((x, y - 1)):
                        root_l, val_l = find(x, y - 1, graph)
                        if root_l not in roots:
                            roots.add(root_l)
                            temp += val_l

                    if graph.get((x, y + 1)):
                        root_r, val_r = find(x, y + 1, graph)
                        if root_r not in roots:
                            roots.add(root_r)
                            temp += val_r

                    result = max(result, temp + 1)
        if result == 0:
            return n * n
        return result


def dfs(x, y, x_root, y_root, graph, grid):
    n = len(grid)
    if x < 0 or x >= n or y < 0 or y >= n or graph.get((x, y)) is not None or grid[x][y] != 1:
        return

    graph[(x, y)] = [(x, y), 1]

    dfs(x - 1, y, x, y, graph, grid)
    dfs(x + 1, y, x, y, graph, grid)
    dfs(x, y - 1, x, y, graph, grid)
    dfs(x, y + 1, x, y, graph, grid)

    if graph.get((x - 1, y)):
        union(x, y, x - 1, y, graph)

    if graph.get((x + 1, y)):
        union(x, y, x + 1, y, graph)

    if graph.get((x, y - 1)):
        union(x, y, x, y - 1, graph)

    if graph.get((x, y + 1)):
        union(x, y, x, y + 1, graph)


def find(x, y, graph):
    p, rank = graph[(x, y)]

    while graph[p][0] != p:
        p = graph[p][0]

    graph[(x, y)] = graph[p]

    return graph[p]


def union(x1, y1, x2, y2, graph):
    x_root, x_rank = find(x1, y1, graph)
    y_root, y_rank = find(x2, y2, graph)
    if x_root != y_root:
        graph[x_root] = [y_root, x_rank + y_rank]
        graph[y_root] = [y_root, x_rank + y_rank]

