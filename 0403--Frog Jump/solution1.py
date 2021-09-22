class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """

        def binary_search(left, right, height):
            while left < right:
                mid = (left + right) // 2
                if stones[mid] < height:
                    left = mid + 1
                elif stones[mid] > height:
                    right = mid
                else:
                    return mid

            if stones[left] == height:
                return left
            else:
                return -1

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
                    nextPos = binary_search(pos + 1, len(stones) - 1, height)
                    if nextPos != -1:
                        res = res or helper(nextPos, jump)
                        if res:
                            cache[(pos, lastJump)] = True
                            return True
            cache[(pos, lastJump)] = res
            return res

        return helper(0, 0)