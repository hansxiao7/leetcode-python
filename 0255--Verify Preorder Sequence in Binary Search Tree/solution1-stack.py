class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        mini = 0
        for i in range(len(preorder)):
            if preorder[i] < mini:
                return False

            while len(stack) != 0 and preorder[i] > stack[-1]:
                mini = stack.pop()

            stack.append(preorder[i])

        return True