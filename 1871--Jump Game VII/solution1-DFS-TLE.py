class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        # DFS
        if s[-1] == '1':
            return False
        n = len(s)
        cache = {}

        def helper(pos, minJump, maxJump, n):
            if cache.get(pos):
                return cache[pos]

            if pos == n - 1:
                cache[n - 1] = True
                return True

            if pos + minJump >= n:
                cache[pos] = False
                return False

            result = False
            for i in range(minJump, maxJump + 1):

                if pos + i >= n:
                    return True
                else:
                    if s[pos + i] == '0':
                        result = result or helper(pos + i, minJump, maxJump, n)
            cache[pos] = result
            return result

        return helper(0, minJump, maxJump, n)