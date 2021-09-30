class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        maps = {}
        names = []
        emails = set()
        for i in range(len(accounts)):
            account = accounts[i]

            if i not in maps:
                maps[i] = i

            names.append(account[0])
            for j in range(1, len(account)):
                email = account[j]
                if email not in maps:
                    maps[email] = i

                else:
                    union(maps[email], i, maps)

                emails.add(email)

        emails = list(emails)
        emails.sort()

        res = []
        posMap = {}

        for email in emails:

            p = find(email, maps)
            if p not in posMap:
                posMap[p] = len(res)
                res.append([accounts[p][0]])

            res[posMap[p]].append(email)

        return res


def find(x, graph):
    p = graph[x]

    while p != graph[p]:
        p = graph[p]

    graph[x] = p

    return p


def union(x, y, graph):
    x_root = find(x, graph)
    y_root = find(y, graph)

    graph[x_root] = y_root