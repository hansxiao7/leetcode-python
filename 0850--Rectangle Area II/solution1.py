class Solution(object):
    def rectangleArea(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: int
        """
        events = []
        for x1, y1, x2, y2 in rectangles:
            events.append([x1, 1, y1, y2])
            events.append([x2, -1, y1, y2])

        events.sort(key=lambda x: (x[0], -x[1]))

        active = []
        prev_x = events[0][0]
        prev_y = 0
        result = 0
        for x, condition, y1, y2 in events:
            result += (x - prev_x) * prev_y

            # add or remove y range
            if condition == 1:
                active.append((y1, y2))
            elif condition == -1:
                active.remove((y1, y2))
            # update y, update_x
            if len(active) == 0:
                total_y = 0
            else:
                active.sort()

                total_y = 0
                i = 0
                end = 0
                while i < len(active) - 1:
                    start = active[i][0]
                    end = active[i][1]

                    while i < len(active) - 1 and active[i + 1][0] < end:
                        end = max(end, active[i + 1][1])
                        i += 1
                    total_y += end - start
                    i += 1
                if end < active[-1][1]:
                    total_y += active[-1][1] - active[-1][0]
            prev_y = total_y
            prev_x = x

        return result % (10 ** 9 + 7)
