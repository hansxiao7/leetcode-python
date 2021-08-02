class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        li = []

        li.append([1000, 'M'])
        li.append([900, 'CM'])
        li.append([500, 'D'])
        li.append([400, 'CD'])
        li.append([100, 'C'])
        li.append([90, 'XC'])
        li.append([50, 'L'])
        li.append([40, 'XL'])
        li.append([10, 'X'])
        li.append([9, 'IX'])
        li.append([5, 'V'])
        li.append([4, 'IV'])
        li.append([1, 'I'])

        result = ''
        point = 0
        while num != 0:
            val = li[point][0]
            s = li[point][1]

            result = result + num // val * s
            num = num % val
            point += 1

        return result