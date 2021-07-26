class Solution(object):
    def maxCompatibilitySum(self, students, mentors):
        """
        :type students: List[List[int]]
        :type mentors: List[List[int]]
        :rtype: int
        """
        return helper(students, mentors, set(), 0)


def helper(s, m, used, i):
    if i >= len(s):
        return 0

    result = 0

    for j in range(len(m)):
        temp_set = used.copy()
        if j in used:
            continue

        score = 0
        for k in range(len(s[0])):
            if s[i][k] == m[j][k]:
                score += 1

        temp_set.add(j)
        result = max(result, score + helper(s, m, temp_set, i + 1))

    return result
