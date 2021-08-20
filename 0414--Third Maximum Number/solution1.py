class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(tuple(nums)))
        if len(nums) < 3:
            return max(nums)

        # quick select
        def partition(left, right):
            rand_id = random.randrange(left, right + 1)
            nums[left], nums[rand_id] = nums[rand_id], nums[left]
            temp = nums[left]

            i = left
            j = right

            while i < j:
                while i < j and nums[j] < temp:
                    j -= 1
                nums[i] = nums[j]

                while i < j and nums[i] > temp:
                    i += 1
                nums[j] = nums[i]

            nums[i] = temp

            return i

        def quick_select(left, right, k):
            if left < right:
                mid = partition(left, right)
                l = mid - left + 1

                if l < k:
                    return quick_select(mid + 1, right, k - l)
                elif l > k:
                    return quick_select(left, mid, k)
                else:
                    return nums[mid]
            else:
                return nums[left]

        return quick_select(0, len(nums) - 1, 3)
