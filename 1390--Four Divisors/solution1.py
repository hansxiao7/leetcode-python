class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        visited = {}
        result = 0

        for i in range(len(nums)):
            temp = nums[i]
            if temp in visited:
                result += visited[temp]
                continue

            temp_li = [1, temp]
            for j in range(2, int(pow(temp, 0.5)) + 1):
                if temp % j == 0:
                    if temp // j == j:
                        temp_li.append(j)
                    else:
                        temp_li.extend([j, temp // j])

                if len(temp_li) > 4:
                    break
            if len(temp_li) == 4:
                visited[temp] = sum(temp_li)
                result += visited[temp]
            else:
                visited[temp] = 0
        return result