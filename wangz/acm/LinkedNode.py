# encoding:utf-8
class ListNode(object):
    """
        1.两个链表逐项相加，形成新的列表
        2.如果相加项大于10，进位
        例：
            [5],[5]->[0,1]
            [1],[9,9]->[0,0,1]
    """
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    ret = ListNode(0)
    p = l1
    q = l2
    carry = 0
    curr = ret
    while (p is not None) or (q is not None):
        if p is not None:
            x = p.val
        else:
            x = 0
        if q is not None:
            y = q.val
        else:
            y = 0
        sum_xy = carry + x + y
        carry = sum_xy / 10
        curr.next = ListNode(sum_xy % 10)
        curr = curr.next
        if p is not None:
            p = p.next
        if q is not None:
            q = q.next

    if carry > 0:
        curr.next = ListNode(carry)
    return ret.next

a1 = ListNode(5)
b1 = ListNode(5)

c = add_two_numbers(a1, b1)
while c is not None:
    print c.val
    c = c.next
