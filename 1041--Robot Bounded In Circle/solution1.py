class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        direction = 0
        x = 0
        y = 0

        for c in instructions:
            if c == 'G':
                if direction == 0:
                    x += 1
                elif direction == 1:
                    y += 1
                elif direction == 2:
                    x -= 1
                else:
                    y -= 1

            elif c == 'R':
                direction = (direction + 1) % 4

            else:  # c = 'L'
                direction = (direction + 3) % 4

        return (x == 0 and y == 0) or (direction != 0)