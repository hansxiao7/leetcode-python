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
        return DFS(maze, visited, start, destination)


def DFS(maze, visited, curr, des):
    if curr == des:
        return True
    up = next_pos(maze, curr, 0)
    down = next_pos(maze, curr, 1)
    left = next_pos(maze, curr, 2)
    right = next_pos(maze, curr, 3)

    visited[curr[0]][curr[1]] = 1

    if visited[up[0]][up[1]] == 0:
        if DFS(maze, visited, up, des):
            return True
    if visited[down[0]][down[1]] == 0:
        if DFS(maze, visited, down, des):
            return True
    if visited[left[0]][left[1]] == 0:
        if DFS(maze, visited, left, des):
            return True
    if visited[right[0]][right[1]] == 0:
        if DFS(maze, visited, right, des):
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