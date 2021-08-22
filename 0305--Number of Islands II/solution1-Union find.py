class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        counts = 0
        graph = {}

        result = []
        neighbors = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for pos in positions:
            x = pos[0]
            y = pos[1]

            if (x, y) in graph:
                result.append(counts)
                continue

            counts += 1

            graph[(x, y)] = (x, y)
            for dx, dy in neighbors:
                new_x = x + dx
                new_y = y + dy

                if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n or (new_x, new_y) not in graph:
                    continue

                if find((new_x, new_y), graph) != find((x, y), graph):
                    counts -= 1
                    union((new_x, new_y), (x, y), graph)

            result.append(counts)
        return result


def find(x, graph):
    p = graph[x]

    while p != graph[p]:
        p = graph[p]

    graph[x] = p

    return p


def union(x, y, graph):
    x_root = find(x, graph)
    y_root = find(y, graph)

    graph[x_root] = y_root