class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        # dfs
        cache = {}
        m = len(price)

        def helper(curr):
            if tuple(curr) in cache:
                return cache[tuple(curr)]
            if sum(curr) == 0:
                return 0

            result = sys.maxint
            for discount in special:
                temp = list(curr)
                cost = discount[-1]
                flag = True
                for i in range(len(discount) - 1):
                    if curr[i] >= discount[i]:
                        temp[i] = curr[i] - discount[i]
                    else:
                        flag = False
                        break

                if flag:
                    result = min(result, cost + helper(temp))

            temp_val = 0
            for i in range(m):
                temp_val += curr[i] * price[i]
            result = min(result, temp_val)

            cache[tuple(curr)] = result

            return result

        return helper(needs)