class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        # DFS brute force
        counts = []
        for i in range(len(strs)):
            word = strs[i]
            count_0 = 0
            count_1 = 0

            for j in range(len(word)):
                if word[j] == '1':
                    count_1 += 1
                else:
                    count_0 += 1
            counts.append((count_0, count_1))

        self.result = 0

        def helper(li, pos, m, n, curr):
            if m < 0 or n < 0:
                return

            self.result = max(self.result, len(curr))

            for i in range(pos, len(li)):
                curr.append(i)
                count_0 = counts[i][0]
                count_1 = counts[i][1]
                helper(li, i + 1, m - count_0, n - count_1, curr)
                curr.pop()

        helper(strs, 0, m, n, [])

        return self.result
