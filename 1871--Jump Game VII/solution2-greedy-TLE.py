class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        if s[n - 1] == '1':
            return False

        last_pos = set()
        last_pos.add(n - 1)

        for i in range(n - 2, -1, -1):
            if s[i] == '0':
                if i + maxJump >= n - 1 and i + minJump <= n - 1:
                    last_pos.add(i)
                    continue
                for j in range(minJump, maxJump + 1):
                    if i + j in last_pos:
                        last_pos.remove(i + j)
                        last_pos.add(i)
        return 0 in last_pos