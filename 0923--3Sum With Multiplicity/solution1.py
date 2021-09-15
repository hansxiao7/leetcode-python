class Solution(object):
    def threeSumMulti(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        counts = {}
        for num in arr:
            counts[num] = counts.get(num, 0) + 1

        keys = counts.keys()

        n = max(counts.values())

        factorial = [1] * (n + 1)
        for i in range(2, n + 1):
            factorial[i] = i * factorial[i - 1]

        def cnk(n, k):
            return factorial[n] / (factorial[n - k] * factorial[k])

        keys.sort()

        res = 0
        for i in range(len(keys)):
            pivot = keys[i]
            if pivot * 3 == target and counts[pivot] >= 3:
                res += (cnk(counts[pivot], 3)) % (10 ** 9 + 7)
            temp = target - pivot
            temp2 = target - 2 * pivot
            if counts[pivot] >= 2 and temp2 in counts and temp2 > pivot:
                res += (cnk(counts[pivot], 2) * counts[temp2]) % (10 ** 9 + 7)

            if temp % 2 == 0 and temp / 2 > pivot:
                if counts.get(temp / 2, 0) >= 2:
                    res += (cnk(counts.get(temp / 2, 0), 2) * counts[pivot]) % (10 ** 9 + 7)
            left = i + 1
            right = len(keys) - 1

            while left < right:
                if keys[left] + keys[right] < temp:
                    left += 1
                elif keys[left] + keys[right] > temp:
                    right -= 1
                else:
                    res += (counts[keys[left]] * counts[keys[right]] * counts[pivot]) % (10 ** 9 + 7)
                    left += 1
                    right -= 1

        return res % (10 ** 9 + 7)

