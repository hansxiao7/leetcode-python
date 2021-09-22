class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        maps = {}

        for i in range(len(stones)):
            maps[stones[i]] = i

        cache = {}

        def helper(pos, lastJump):
            if (pos, lastJump) in cache:
                return cache[(pos, lastJump)]

            if pos >= len(stones):
                return False

            if pos == len(stones) - 1:
                return True

            res = False
            nextJump = [lastJump - 1, lastJump, lastJump + 1]

            for jump in nextJump:
                if jump > 0:
                    # find the next pos
                    height = stones[pos] + jump
                    if height in maps:
                        nextPos = maps[height]
                        res = res or helper(nextPos, jump)
                        if res:
                            cache[(pos, lastJump)] = True
                            return True
            cache[(pos, lastJump)] = res
            return res

        return helper(0, 0)