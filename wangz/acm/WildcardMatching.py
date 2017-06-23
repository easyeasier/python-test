# encoding:utf-8
class WildcardMatching(object):
    @staticmethod
    def is_match(s, p):
        """
        
        :param s: String 
        :param p: String
        :return: boolean
        """
        index_s = index_p = index_match = 0  # s,p代表当前匹配的位置，match代表匹配的起始位置
        index_star = -1
        while index_s < len(s):
            if index_p < len(p) and (s[index_s] == p[index_p] or p[index_p] == '?'):
                index_s += 1
                index_p += 1
            elif index_p < len(p) and p[index_p] == '*':
                index_star = index_p
                index_p += 1
                index_match = index_s
            elif index_star != -1:
                index_match += 1
                index_s = index_match
                index_p = index_star + 1
            else:
                return False

        while index_p < len(p) and p[index_p] == '*':
            index_p += 1

        return index_p == len(p)


if __name__ == "__main__":
    wm = WildcardMatching()

    s = "aa";
    p = "a";
    print "s = " + s + ", p = " + p + ",ret = " + str(wm.is_match(s, p))
    s = "aa";
    p = "aa";
    print "s = " + s + ", p = " + p + ",ret = " + str(wm.is_match(s, p))
    s = "aaa";
    p = "aa";
    print "s = " + s + ", p = " + p + ",ret = " + str(wm.is_match(s, p))
    s = "aa";
    p = "*";
    print "s = " + s + ", p = " + p + ",ret = " + str(wm.is_match(s, p))
    s = "mississippi";
    p = "m*issi*iss*";
    print "s = " + s + ", p = " + p + ",ret = " + str(wm.is_match(s, p))
    s = "mississippi";
    p = "m*issi*ppi*";
    print "s = " + s + ", p = " + p + ",ret = " + str(wm.is_match(s, p))
    s = "aa";
    p = "a*";
    print "s = " + s + ", p = " + p + ",ret = " + str(wm.is_match(s, p))
    s = "aa";
    p = "?*";
    print "s = " + s + ", p = " + p + ",ret = " + str(wm.is_match(s, p))
    s = "aab";
    p = "c*a*b";
    print "s = " + s + ", p = " + p + ",ret = " + str(wm.is_match(s, p))
    s = "aab";
    p = "a*b*";
    print "s = " + s + ", p = " + p + ",ret = " + str(wm.is_match(s, p))
    s = "aab";
    p = "a*b*b*";
    print "s = " + s + ", p = " + p + ",ret = " + str(wm.is_match(s, p))
    s = "aabc";
    p = "a*b*";
    print "s = " + s + ", p = " + p + ",ret = " + str(wm.is_match(s, p))
    s = "aaaa";
    p = "***a";
    print "s = " + s + ", p = " + p + ",ret = " + str(wm.is_match(s, p))
