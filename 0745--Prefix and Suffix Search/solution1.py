class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

    def addWord(self, word):
        node = self
        for c in word:
            if node.children.get(ord(c) - ord('a')) is None:
                node.children[ord(c) - ord('a')] = TrieNode()

            node = node.children[ord(c) - ord('a')]
        node.end = True


class WordFilter(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.maps = {}
        self.head = TrieNode()

        for i in range(len(words)):
            word = words[i]
            self.maps[word] = i

            word = '#' + word
            self.head.addWord(word)

            suffix = ''
            for j in range(len(word) - 1, 0, -1):
                suffix = word[j] + suffix
                self.head.addWord(suffix + word)

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        temp = suffix + '#' + prefix

        node = self.head
        res = []

        for c in temp:
            if node.children.get(ord(c) - ord('a')) is None:
                return -1
            node = node.children[ord(c) - ord('a')]

        def helper(curr, node):
            if node.end:
                res.append(curr)

            for key in node.children.keys():
                c = chr(key + ord('a'))
                helper(curr + c, node.children[key])

        helper(prefix, node)
        result = -1

        for word in res:
            if self.maps[word] > result:
                result = self.maps[word]

        return result

# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)