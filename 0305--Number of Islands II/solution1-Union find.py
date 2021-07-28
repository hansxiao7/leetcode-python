class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        # union find
        graph = {}
        roots = set()
        result = []

        for pos in positions:
            x = pos[0]
            y = pos[1]
            pos_id = x * n + y

            if graph.get(pos_id):
                result.append(result[-1])
                continue
            graph[pos_id] = pos_id
            roots.add(pos_id)

            if x - 1 >= 0 and graph.get((x - 1) * n + y) is not None:
                union(pos_id, (x - 1) * n + y, graph, roots)

            if x + 1 < m and graph.get((x + 1) * n + y) is not None:
                union(pos_id, (x + 1) * n + y, graph, roots)

            if y - 1 >= 0 and graph.get(pos_id - 1) is not None:
                union(pos_id, pos_id - 1, graph, roots)

            if y + 1 < n and graph.get(pos_id + 1) is not None:
                union(pos_id, pos_id + 1, graph, roots)

            result.append(len(roots))

        return result


def find(x, graph):
    p = graph[x]

    while graph[p] != p:
        p = graph[p]

    graph[x] = p

    return p


def union(x, y, graph, roots):
    x_root = find(x, graph)
    y_root = find(y, graph)
    roots.remove(x_root)
    roots.add(y_root)

    graph[x_root] = y_root