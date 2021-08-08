class Solution(object):
    def generatePossibleNextMoves(self, currentState):
        """
        :type currentState: str
        :rtype: List[str]
        """
        if len(currentState) < 2:
            return []

        result = []

        for i in range(len(currentState) - 1):
            if currentState[i] == currentState[i + 1] and currentState[i] == '+':
                result.append(currentState[:i] + '--' + currentState[i + 2:])

        return result