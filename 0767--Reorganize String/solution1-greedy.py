import heapq


class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # bucket/count sort
        bucket = {}

        for i in range(len(s)):
            bucket[s[i]] = bucket.get(s[i], 0) + 1

        result = ''

        heap = []

        for key in bucket.keys():
            heapq.heappush(heap, (-bucket[key], key))

        while len(heap) != 0:
            val, c = heapq.heappop(heap)

            if result != '' and c == result[-1]:
                if len(heap) == 0:
                    return ""
                else:
                    new_val, new_c = heapq.heappop(heap)
                    heapq.heappush(heap, (val, c))
                    val = new_val
                    c = new_c

            result += c
            val += 1

            if val < 0:
                heapq.heappush(heap, (val, c))

        return result

