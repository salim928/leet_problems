class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #sign = -1 if x < 0 else 1
        #rev = int(str(abs(x))[::-1]) * sign
        #return rev if -2**31 <= rev <= 2**31 - 1 else 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        res = 0

        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            digit = x % 10  # get the last digit
            x //= 10        # remove the last digit

           
            if res > (INT_MAX - digit) // 10:
                return 0

            res = res * 10 + digit

        return sign * res    