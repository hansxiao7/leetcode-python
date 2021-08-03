class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        # BFS
        # Children: A or R
        queue = collections.deque()
        queue.append((0, 1))  # pos, speed

        result = 0
        while len(queue) != 0:
            n = len(queue)

            for i in range(n):
                pos, speed = queue.popleft()

                if pos == target:
                    return result

                queue.append((pos + speed, speed * 2))

                if (pos + speed > target and speed > 0) or (pos + speed < target and speed < 0):
                    queue.append((pos, -abs(speed) / speed))

            result += 1

