class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        self.d = self.build_dict(words)
        all_keys = self.d.keys()
        top_k_keys = all_keys[:k]

        # build the heap
        for i in range((k - 2) // 2, -1, -1):
            self.sift(top_k_keys, i, k - 1)

        # iterate over all other keys
        for j in range(k, len(all_keys)):
            if self.compare(all_keys[j], top_k_keys[0]) == 1:
                top_k_keys[0] = all_keys[j]
                self.sift(top_k_keys, 0, k - 1)

        # output the result
        for m in range(k - 1, -1, -1):
            top_k_keys[0], top_k_keys[m] = top_k_keys[m], top_k_keys[0]
            self.sift(top_k_keys, 0, m - 1)

        return top_k_keys

    def build_dict(self, words):
        result = {}

        for i in range(len(words)):
            if result.get(words[i]) is None:
                result[words[i]] = 1
            else:
                result[words[i]] += 1

        return result

    def compare(self, left_key, right_key):
        if self.d[left_key] > self.d[right_key]:
            return 1
        elif self.d[left_key] < self.d[right_key]:
            return -1
        else:
            if left_key < right_key:
                return 1
            else:
                return -1

    def sift(self, li, low, high):
        i = low
        j = 2 * i + 1

        while j <= high:
            if j + 1 <= high and self.compare(li[j + 1], li[j]) == -1:
                j = j + 1

            if self.compare(li[i], li[j]) == 1:
                li[i], li[j] = li[j], li[i]
                i = j
                j = 2 * i + 1
            else:
                break