class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        reversed_str = str(abs(x))[::-1]
        reversed_num = sign * int(reversed_str)
        if -2**31 <= reversed_num <= 2**31 - 1:
            return reversed_num
        return 0
            