class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        root = TrieNode()
        for word in products:
            node = root

            for c in word:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]

            node.end = True

        def bfs(node, prev):
            if node is None:
                return []
            queue = collections.deque()
            queue.append((node, prev))

            res = []

            while len(queue) != 0:
                node, s = queue.popleft()

                if node.end:
                    res.append(s)
                children = node.children

                for key in children.keys():
                    queue.append((children[key], s + key))

            res.sort()
            if len(res) > 3:
                return res[:3]
            return res

        node = root
        res = []
        prev = ''
        for c in searchWord:
            temp = []
            prev = prev + c

            if node is not None:
                node = node.children.get(c, None)

            res.append(bfs(node, prev))

        return res

