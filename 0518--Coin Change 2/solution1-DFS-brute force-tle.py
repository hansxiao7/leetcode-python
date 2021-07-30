class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        # DFS
        return dfs(amount, len(coins) - 1, coins)


def dfs(y, pos, coins):  # 避免重复，y为剩余amount, pos为当前使用最大硬币的位置
    if y == 0:
        return 1
    if y < 0:
        return 0

    result = 0
    for i in range(pos + 1):
        c = coins[i]
        result += dfs(y - c, i, coins)

    return result