class Solution(object):
    def latestDayToCross(self, row, col, cells):
        """
        :type row: int
        :type col: int
        :type cells: List[List[int]]
        :rtype: int
        """
        graph = {}
        last_row = set()
        for i in range(len(cells) - 1, -1, -1):
            pos = tuple(cells[i])
            x, y = pos
            graph[pos] = pos, pos[0]

            u = x - 1, y
            d = x + 1, y
            l = x, y - 1
            r = x, y + 1

            if u in graph:
                union(pos, u, graph)
            if d in graph:
                union(pos, d, graph)
            if l in graph:
                union(pos, l, graph)
            if r in graph:
                union(pos, r, graph)

            if x == row:
                last_row.add(pos)

            for temp in last_row:
                find(temp, graph)
                if graph[temp][1] == 1:
                    return i


def find(x, graph):
    p, rank = graph[x]
    while graph[p][0] != p:
        p = graph[p][0]

    graph[x] = graph[p]

    return graph[p]


def union(x, y, graph):
    x_root, x_rank = find(x, graph)
    y_root, y_rank = find(y, graph)

    graph[x_root] = x_root, min(x_rank, y_rank)
    graph[y_root] = x_root, min(x_rank, y_rank)