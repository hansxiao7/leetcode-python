class Solution(object):
    def findSmallestRegion(self, regions, region1, region2):
        """
        :type regions: List[List[str]]
        :type region1: str
        :type region2: str
        :rtype: str
        """
        dict1 = {}
        for region in regions:
            y = region[0]
            for i in range(1, len(region)):
                dict1[region[i]] = y

        path1 = []
        path2 = []

        node = region1
        while node:
            path1.append(node)
            node = dict1.get(node, None)

        node = region2
        while node:
            path2.append(node)
            node = dict1.get(node, None)

        p1 = len(path1) - 1
        p2 = len(path2) - 1

        while p1 >= 0 and p2 >= 0:
            if path1[p1] == path2[p2]:
                p1 -= 1
                p2 -= 1
                continue
            else:
                return path1[p1 + 1]

        if p1 < 0:
            return region1
        else:
            return region2



