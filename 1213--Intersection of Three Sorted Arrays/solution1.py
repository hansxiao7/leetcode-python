class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        n = len(arr1)
        l = 0
        m = 0
        r = 0

        res = []
        while l < n and m < n and r < n:
            temp = max(arr1[l], arr2[m], arr3[r])

            while l < n and arr1[l] < temp:
                l += 1

            while m < n and arr2[m] < temp:
                m += 1

            while r < n and arr3[r] < temp:
                r += 1

            if l < n and m < n and r < n and arr1[l] == arr2[m] and arr2[m] == arr3[r]:
                res.append(arr1[l])
                l += 1
                m += 1
                r += 1

        return res
