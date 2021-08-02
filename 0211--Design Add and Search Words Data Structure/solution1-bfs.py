class TreeNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.end = False


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root
        for s in word:
            if node.children[ord(s) - ord('a')] is None:
                node.children[ord(s) - ord('a')] = TreeNode()
            node = node.children[ord(s) - ord('a')]
        node.end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        queue = [self.root]

        for s in word:
            n = len(queue)
            if n == 0:
                return False
            for i in range(n):
                node = queue.pop(0)
                if s != '.':
                    if node.children[ord(s) - ord('a')]:
                        queue.append(node.children[ord(s) - ord('a')])
                else:
                    for j in node.children:
                        if j:
                            queue.append(j)

        if len(queue) == 0:
            return False

        for i in range(len(queue)):
            if queue[i].end:
                return True

        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)