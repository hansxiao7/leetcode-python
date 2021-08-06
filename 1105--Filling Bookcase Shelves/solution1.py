class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        n = len(books)
        dp = [sys.maxint for _ in range(n + 1)]
        dp[0] = 0
        dp[1] = books[0][1]

        for i in range(2, n + 1):
            curr_width = 0
            curr_height = 0
            for j in range(i, 0, -1):
                curr_width += books[j - 1][0]
                curr_height = max(curr_height, books[j - 1][1])
                if curr_width > shelf_width:
                    break
                dp[i] = min(dp[i], dp[j - 1] + curr_height)

        return dp[n]



