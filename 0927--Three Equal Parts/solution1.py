class Solution(object):
    def threeEqualParts(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        # get the sum of the whole array
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return [-1, -1]

        if total_sum == 0:
            return [0, len(arr) - 1]

        count = 0
        T = total_sum / 3
        s_loc = []
        e_loc = []
        m = 0
        n = 0
        for i in range(len(arr)):
            if arr[i] == 1:
                count += 1
            if count == T * m + 1:
                s_loc.append(i)
                m += 1
            if count == (n + 1) * T:
                e_loc.append(i)
                n += 1

        num_zeros = len(arr) - 1 - e_loc[2]
        if e_loc[0] - s_loc[0] == e_loc[1] - s_loc[1] and e_loc[0] - s_loc[0] == e_loc[2] - s_loc[2]:
            if e_loc[0] + num_zeros < s_loc[1] and e_loc[1] + num_zeros < s_loc[2]:
                return [e_loc[0] + num_zeros, e_loc[1] + num_zeros + 1]

        return [-1, -1]