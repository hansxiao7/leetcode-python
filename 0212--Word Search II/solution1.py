class TrieNode:
    def __init__(self, s=None):
        self.end = False
        self.children = [None for _ in range(26)]
        self.s = s

    def get(self, s):
        return self.children[ord(s) - ord('a')]


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        m = len(board)
        n = len(board[0])

        result = set()
        # build a trie tree
        root = TrieNode()
        for word in words:
            node = root
            for i in range(len(word)):
                if node.children[ord(word[i]) - ord('a')] is None:
                    node.children[ord(word[i]) - ord('a')] = TrieNode(s=word[i])
                node = node.children[ord(word[i]) - ord('a')]
            node.end = True

        result = []
        visited = set()
        for i in range(m):
            for j in range(n):
                curr_word = ''
                helper(i, j, board, visited, root, curr_word, result)
        return result


def helper(x, y, board, visited, node, curr_word, result):
    m = len(board)
    n = len(board[0])

    if node is None:
        return

    if x < 0 or x >= m or y < 0 or y >= n or (x, y) in visited:
        return

    child = node.get(board[x][y])
    if child is None:
        return
    curr_word = curr_word + child.s

    visited.add((x, y))
    if child.end:
        result.append(curr_word)
        child.end = False

    helper(x - 1, y, board, visited, child, curr_word, result)
    helper(x + 1, y, board, visited, child, curr_word, result)
    helper(x, y - 1, board, visited, child, curr_word, result)
    helper(x, y + 1, board, visited, child, curr_word, result)

    visited.remove((x, y))
