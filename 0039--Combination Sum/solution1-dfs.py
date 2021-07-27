class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        return dfs(0, candidates, target)


def dfs(k, candidates, target):
    if target == 0:
        return [[]]

    if target < 0:
        return []

    result = []

    for i in range(k, len(candidates)):
        temp2 = dfs(i, candidates, target - candidates[i])
        for j in range(len(temp2)):
            temp1 = [candidates[i]]
            temp1.extend(temp2[j])
            result.append(temp1)

    return result