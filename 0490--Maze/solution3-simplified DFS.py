class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        m = len(maze)
        n = len(maze[0])
        visited = [[0 for j in range(n)] for i in range(m)]

        # DFS
        return DFS(visited, maze, start, destination)


def DFS(visited, maze, p, goal):
    if p == goal:
        return True

    visited[p[0]][p[1]] = 1

    for i in range(4):
        next_p = next_pos(maze, p, i)
        if visited[next_p[0]][next_p[1]] == 0:
            if DFS(visited, maze, next_p, goal):
                return True
    return False


def next_pos(maze, curr, action):
    m = len(maze)
    n = len(maze[0])
    result = [curr[0], curr[1]]
    if action == 0:  # up
        while result[0] > 0 and maze[result[0] - 1][result[1]] != 1:
            result[0] -= 1

    elif action == 1:  # down
        while result[0] < m - 1 and maze[result[0] + 1][result[1]] != 1:
            result[0] += 1

    elif action == 2:  # left
        while result[1] > 0 and maze[result[0]][result[1] - 1] != 1:
            result[1] -= 1

    elif action == 3:  # right
        while result[1] < n - 1 and maze[result[0]][result[1] + 1] != 1:
            result[1] += 1

    return result