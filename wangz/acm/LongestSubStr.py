# encoding:utf-8
class LongestSubStr(object):
    """
        longest substring without repeating characters
        求最大子串，子串内没有重复的字符
        思路：
          1.遍历每个字符存入dict，记录start和end结点
          2.如果当前字符有重复字符存在，判断长度是否比最大子串长
          3.从重复字符的下一个字符，当做新的子串的起点
        注意：
          1.因为只用一个dict，在当前子串内可能会查到起始点之前的字符，需要排除
            （tmmzuxt t在最大子串mzuxt中重复，但应该排除第一个t）
        优化项：
          1.当start重新赋值时，其后到结尾的子串长度也不会当前的最大子串长度，所以，可以不在计算
    """

    def length_of_longest_substring(self, s):
        if s is None or len(s) is 0:
            return 0
        length = len(s)

        if length is 1:
            return 1

        start = 0
        end = 1
        max_length = 1
        char_dict = {s[start]: 0}

        while end < length:
            repeating_index = char_dict.get(s[end])
            if repeating_index is not None and repeating_index >= start:
                start = repeating_index + 1
                if (length - start + 1) <= max_length:
                    break
            else:
                max_length = max(max_length, end - start + 1)

            char_dict[s[end]] = end
            end += 1
        return max_length


print LongestSubStr().length_of_longest_substring("abcabcbb")  # abc
print LongestSubStr().length_of_longest_substring("pwwkew")  # wke
print LongestSubStr().length_of_longest_substring("tmmzuxt")  # mzuxt
