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

        def dfs(word, node):
            for i in range(len(word)):
                s = word[i]
                if s != '.':
                    if node.children[ord(s) - ord('a')]:
                        node = node.children[ord(s) - ord('a')]
                    else:
                        return False

                else:
                    temp = False
                    for child in node.children:
                        if child:
                            if dfs(word[i + 1:], child):
                                return True
                    return False
            return node.end

        return dfs(word, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)