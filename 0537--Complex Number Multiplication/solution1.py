class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        def get_num(s, i, operator, li):
            num = 0
            while i < len(s) and s[i].isnumeric():
                num = num * 10 + int(s[i])
                i += 1

            if operator == '+':
                li.append(num)
            else:
                li.append(-num)

            return i

        def helper(s, li):
            if s[0].isnumeric():
                operator = '+'
                i = 0
            else:
                operator = s[0]
                i = 1

            i = get_num(s, i, operator, li)

            # get the complex number
            operator = '+'
            if s[i + 1].isnumeric():
                i = i + 1
            else:
                operator = s[i + 1]
                i = i + 2
            get_num(s, i, operator, li)

        li1 = []
        li2 = []
        helper(num1, li1)
        helper(num2, li2)

        result = ''
        result = str(li1[0] * li2[0] - li1[1] * li2[1]) + '+' + str(li1[1] * li2[0] + li1[0] * li2[1]) + 'i'

        return str(result)