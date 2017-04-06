# encoding:utf-8
import sys
class Solution(object):
    """
        回文int数值，，默认负数是不能回文的
    """
    def reverse_integer(self, x):
        """
        :type x: int
        :rtype: int
        """
        current = 0

        while x > 0:
            temp = x % 10
            current = current * 10 + temp
            x /= 10
        current += x
        if current > sys.maxint:
            return 0
        else:
            return current

    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x == self.reverse_integer(x):
            return True
        else:
            return False


print Solution().isPalindrome(12344321)
