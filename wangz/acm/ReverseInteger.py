def reverse_integer(x):
    """
    :type x: int
    :rtype: int
    """
    current = 0

    flag = False
    if x < 0:
        flag = True
        x = abs(x)
    while x > 0:
        temp = x % 10
        current = current * 10 + temp
        x /= 10
    abs_value = current + x
    if abs_value > 2147483647:
        return 0
    elif flag is False:
        return abs_value
    else:
        return 0 - abs_value


