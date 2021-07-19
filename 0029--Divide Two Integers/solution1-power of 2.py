class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        else:
            sign = 1

        a = abs(dividend)
        b = abs(divisor)

        MAX_INT = 2147483647  # 2**31 - 1
        MIN_INT = -2147483648  # -2**31

        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        power = 1
        result = 0
        while a >= abs(divisor):

            while a >= b:
                last_b = b
                b += b

                last_power = power
                power += power
            a = a - last_b
            b = abs(divisor)
            power = 1
            result += last_power

        if sign == 1:
            return result
        else:
            return -result




