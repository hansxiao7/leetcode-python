class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []

        def helper(s, k, curr, start, end):
            if start > end:
                return

            if k == 0 and start <= end:
                if check_palindrome(s, start, end):
                    result.append(list(curr) + [s[start:end + 1]])
                return

            for pos in range(start, end + 1):
                if check_palindrome(s, start, pos):
                    curr.append(s[start:pos + 1])
                    helper(s, k - 1, curr, pos + 1, end)
                    curr.pop()

        for k in range(len(s)):
            helper(s, k, [], 0, len(s) - 1)

        return result


def check_palindrome(s, start, end):
    n = end + 1 - start
    for i in range(start, start + n // 2):
        if s[i] == s[end + start - i]:
            continue
        else:
            return False

    return True


