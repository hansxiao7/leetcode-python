class Solution(object):
    def deleteTreeNodes(self, nodes, parent, value):
        """
        :type nodes: int
        :type parent: List[int]
        :type value: List[int]
        :rtype: int
        """

        maps = {}

        for i in range(len(parent)):
            if parent[i] == -1:
                continue
            if parent[i] not in maps:
                maps[parent[i]] = []
            maps[parent[i]].append(i)

        def helper(node):
            if node not in maps:
                if value[node] == 0:
                    return 0, 0
                else:
                    return 1, value[node]

            children = maps.get(node, [])

            counts = 1
            sumValue = value[node]
            for i in range(len(children)):
                child = children[i]
                childCount, childSum = helper(child)
                counts += childCount
                sumValue += childSum

            if sumValue == 0:
                return 0, 0
            else:
                return counts, sumValue

        res, _ = helper(0)
        return res