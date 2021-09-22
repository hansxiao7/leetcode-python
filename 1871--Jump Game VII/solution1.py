class Solution(object):
    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        # find the index for all 0s
        zeros = []
        for i in range(len(s)):
            if s[i] == '0':
                zeros.append(i)

        queue = collections.deque()
        queue.append(0)
        for i in range(1, len(zeros)):
            while len(queue) != 0 and zeros[i] - queue[0] > maxJump:
                queue.popleft()

            if len(queue) != 0 and zeros[i] - queue[0] >= minJump:
                queue.append(zeros[i])
                if zeros[i] == len(s) - 1:
                    return True

            if len(queue) == 0:
                return False

        return False