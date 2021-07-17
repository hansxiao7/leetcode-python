class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :type nums4: List[int]
        :rtype: int
        """
        dict1 = build_dict(nums1, nums2)
        dict2 = build_dict(nums3, nums4)

        count = 0
        for i in dict1.keys():
            if dict2.get(-i) is not None:
                count += len(dict1[i]) * len(dict2[-i])

        return count


def build_dict(li1, li2):
    dict1 = {}

    for i in range(len(li1)):
        for j in range(len(li2)):
            if dict1.get(li1[i] + li2[j]) is None:
                dict1[li1[i] + li2[j]] = [[i, j]]
            else:
                dict1[li1[i] + li2[j]].append([i, j])

    return dict1
