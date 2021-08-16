class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0

        counts = {}
        count = 0
        result = 0

        for right in range(len(fruits)):
            if counts.get(fruits[right], 0) == 0:
                count += 1
            counts[fruits[right]] = counts.get(fruits[right], 0) + 1
            while count > 2:
                counts[fruits[left]] -= 1
                if counts[fruits[left]] == 0:
                    count -= 1
                left += 1

            result = max(result, right - left + 1)

        return result