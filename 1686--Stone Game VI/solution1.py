class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        n = len(aliceValues)
        values = [(aliceValues[i] + bobValues[i], i) for i in range(n)]
        values.sort()
        values.reverse()
        alice_v = 0
        bob_v = 0
        for i in range(0, n, 2):
            _, a_id = values[i]
            alice_v += aliceValues[a_id]
        for j in range(1, n, 2):
            _, b_id = values[j]
            bob_v += bobValues[b_id]
        if alice_v > bob_v:
            return 1
        elif alice_v < bob_v:
            return -1
        else:
            return 0