class FindSumPairs(object):

    def __init__(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        """
        self.nums1 = nums1
        self.nums2 = nums2

        self.count_2 = {}

        for i in range(len(nums2)):
            self.count_2[nums2[i]] = self.count_2.get(nums2[i], 0) + 1

    def add(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.count_2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.count_2[self.nums2[index]] = self.count_2.get(self.nums2[index], 0) + 1

    def count(self, tot):
        """
        :type tot: int
        :rtype: int
        """
        result = 0
        dict1 = self.count_2
        li = self.nums1

        for i in range(len(li)):
            if dict1.get(tot - li[i]):
                result += dict1.get(tot - li[i])

        return result

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)