Python 3.8.8 (tags/v3.8.8:024d805, Feb 19 2021, 13:18:16) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        self.d = self.build_dict(nums)
        total_d_keys = self.d.keys()
        d_keys = total_d_keys[:k]
        # build the heap
        for i in range((k-2)//2, -1, -1):
            self.sift(d_keys, i, k-1)
        
        for j in range(k, len(total_d_keys)):
            if self.d[total_d_keys[j]] > self.d[d_keys[0]]:
                d_keys[0] = total_d_keys[j]
                self.sift(d_keys, 0, k-1)
        
        # output the results
        for m in range(k-1, -1, -1):
            d_keys[0], d_keys[m] = d_keys[m], d_keys[0]
            self.sift(d_keys, 0, m-1)
        
        return d_keys
        
        
    def build_dict(self, nums):
        result = {}
        for i in range(len(nums)):
            if result.get(nums[i]) is None:
                result[nums[i]] = 1
            else:
                result[nums[i]] += 1
        
        return result
                
    def sift(self, d_keys, low, high):
        i = low
        j = 2 * i + 1
        
        while j <= high:
            if j + 1 <= high and self.d[d_keys[j+1]] < self.d[d_keys[j]]:
                j = j + 1
            
            if self.d[d_keys[j]] < self.d[d_keys[i]]:
                d_keys[i], d_keys[j] = d_keys[j], d_keys[i]
                i = j
                j = 2 * i + 1
            else:
                break
        
        