# encoding:utf-8
"""
问题：longest_palindromic_substring 最大回文子串
思路:1. 直接的解决方法，双向遍历，取两正倒序两数组的最大相同子串
    2. 本文采用的另一种方法：
        2.1回文子串特点，中间点相同的向两边同步扩散。
        2.2对每一个字符进行两天扩散，回文遍历
        2.3分别采用奇数回文和偶数回文，求最大的值
"""


def longest_palindromic_substring(s):
    length = len(s)
    if length is 1:
        return s
    i = 1
    max_len = 1
    start = 0
    end = 0
    while i < length:
        left = i
        right = i
        while left >= 0 and right < length:
            if s[left] is s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    start = left
                    end = right
                left -= 1
                right += 1
            else:
                break

        left = i - 1
        right = i
        while left >= 0 and right < length:
            if s[left] is s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    start = left
                    end = right
                left -= 1
                right += 1
            else:
                break

        i += 1

    return s[start:end + 1]


str = "babad"
print longest_palindromic_substring(str)
str = "ccc"
print longest_palindromic_substring(str)
