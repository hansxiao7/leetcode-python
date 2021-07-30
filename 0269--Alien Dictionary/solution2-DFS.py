class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # build the graph
        word_li = []
        graph = {}

        for word in words:
            for i in range(len(word)):
                word_li.append(word[i])

        for i in range(len(words) - 1):
            curr = words[i]
            next = words[i + 1]

            n = min(len(curr), len(next))
            if curr[:n] == next[:n] and len(curr) > len(next):
                return ''

            for j in range(n):
                if curr[j] == next[j]:
                    continue
                else:
                    if graph.get(curr[j]) is None:
                        graph[curr[j]] = [next[j]]
                    else:
                        graph[curr[j]].append(next[j])
                    break

        # DFS with visited and visiting
        visited = set()
        visiting = set()
        result = []

        for i in range(len(word_li)):
            x = word_li[i]
            if x not in visited and x not in visiting:
                flag = dfs(x, visited, visiting, graph, result)
                if flag == False:
                    return ''

        return ''.join(result)


def dfs(x, visited, visiting, graph, result):
    if x in visited:
        return True
    if x in visiting:
        return False

    visiting.add(x)

    children = graph.get(x, [])

    for i in range(len(children)):
        child = children[i]
        if child not in visited:
            flag = dfs(child, visited, visiting, graph, result)
            if flag == False:
                return False

    visiting.remove(x)
    visited.add(x)

    result.insert(0, x)

    return True
