class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        m_min = m
        n_min = n

        for op in ops:
            m_min = min(m_min, op[0])
            n_min = min(n_min, op[1])

        return m_min * n_min