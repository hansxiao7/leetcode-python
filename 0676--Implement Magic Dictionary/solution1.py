class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dictset = {}

    def buildDict(self, dictionary):
        """
        :type dictionary: List[str]
        :rtype: None
        """
        for word in dictionary:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                if key not in self.dictset:
                    self.dictset[key] = set()

                self.dictset[key].add(word)

    def search(self, searchWord):
        """
        :type searchWord: str
        :rtype: bool
        """
        for i in range(len(searchWord)):
            key = searchWord[:i] + '*' + searchWord[i + 1:]
            children = self.dictset.get(key, set())
            for word in children:
                if word != searchWord:
                    return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)