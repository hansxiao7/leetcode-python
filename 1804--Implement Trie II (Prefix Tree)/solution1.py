class TrieNode:
    def __init__(self):
        self.val = [None] * 26
        self.end = 0
        self.count = 0


class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root

        for c in word:
            if node.val[ord(c) - ord('a')] is None:
                node.val[ord(c) - ord('a')] = TrieNode()
            node.val[ord(c) - ord('a')].count += 1
            node = node.val[ord(c) - ord('a')]

        node.end += 1

    def countWordsEqualTo(self, word):
        """
        :type word: str
        :rtype: int
        """
        node = self.root

        for c in word:
            if node.val[ord(c) - ord('a')] is None:
                return 0
            node = node.val[ord(c) - ord('a')]

        return node.end

    def countWordsStartingWith(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root

        for c in prefix:
            if node.val[ord(c) - ord('a')] is None:
                return 0
            node = node.val[ord(c) - ord('a')]

        return node.count

    def erase(self, word):
        """
        :type word: str
        :rtype: None
        """
        node = self.root

        for c in word:
            node.val[ord(c) - ord('a')].count -= 1
            node = node.val[ord(c) - ord('a')]

        node.end -= 1

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.countWordsEqualTo(word)
# param_3 = obj.countWordsStartingWith(prefix)
# obj.erase(word)