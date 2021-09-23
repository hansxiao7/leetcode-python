class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m = len(image)
        n = len(image[0])

        target = image[sr][sc]

        if target == newColor:
            return image

        move = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def helper(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or image[x][y] != target:
                return

            image[x][y] = newColor

            for dx, dy in move:
                helper(x + dx, y + dy)

        helper(sr, sc)

        return image


