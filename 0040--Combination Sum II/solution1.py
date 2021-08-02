class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []

        helper(0, candidates, [], target, result)

        return result


def helper(pos, li, curr, target, result):
    if target < 0:
        return

    if target == 0:
        result.append(curr)
        return

    for i in range(pos, len(li)):
        if i != pos and li[i - 1] == li[i]:
            continue
        helper(i + 1, li, curr + [li[i]], target - li[i], result)


