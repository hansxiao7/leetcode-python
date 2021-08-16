class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        temp = []

        def binary_search(left, right, target):
            if left < right:
                mid = (left + right) // 2
                if temp[mid] > target:
                    return binary_search(left, mid, target)
                elif temp[mid] < target:
                    return binary_search(mid + 1, right, target)
                else:
                    return mid
            else:
                if temp[left] < target:
                    return left + 1
                return left

        for i in range(len(envelopes)):
            if temp == [] or envelopes[i][1] > temp[-1]:
                temp.append(envelopes[i][1])
            else:
                pos = binary_search(0, len(temp) - 1, envelopes[i][1])
                temp[pos] = envelopes[i][1]
        return len(temp)