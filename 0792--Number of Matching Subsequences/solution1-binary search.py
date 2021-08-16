class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        target = {}
        visited = {}

        for i in range(len(s)):
            if s[i] not in target:
                target[s[i]] = []
            target[s[i]].append(i)

        result = 0

        for word in words:
            if word in visited:
                result += visited[word]
                continue
            temp = {}
            flag = True
            prev_pos = -1
            for i in range(len(word)):
                if word[i] not in target:
                    flag = False
                    break
                pos = target[word[i]]
                new_pos = binary_search(pos, 0, len(pos) - 1, prev_pos)
                if new_pos >= len(pos):
                    flag = False
                    break
                prev_pos = pos[new_pos]

            if flag:
                result += 1
                visited[word] = 1
            else:
                visited[word] = 0

        return result


def binary_search(li, left, right, target):
    if left < right:
        mid = (left + right) // 2
        if li[mid] <= target:
            return binary_search(li, mid + 1, right, target)
        else:
            return binary_search(li, left, mid, target)
    else:
        if li[left] <= target:
            return left + 1
        return left