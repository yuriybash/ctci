class Node(object):

    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = next_

    def __repr__(self):
        return 'Node(x=%s)' % self.val


def sum_lists(a, b):

    power = 1
    node = a
    first_num = 0
    while node:
        first_num += node.val*power
        power *= 10
        node = node.next_

    power = 1
    node = b
    second_num = 0
    while node:
        second_num += node.val*power
        power *= 10
        node = node.next_

    return first_num + second_num


def sum_lists_backwards(a, b):

    node = a
    power_a = -1
    first_num = 0
    while node:
        power_a += 1
        node = node.next_
    node = a
    while node:
        first_num += node.val * pow(10, power_a)
        power_a -= 1
        node = node.next_

    node = b
    power_b = -1
    second_num = 0
    while node:
        power_b += 1
        node = node.next_
    node = b
    while node:
        second_num += node.val * pow(10, power_b)
        power_b -= 1
        node = node.next_

    return first_num + second_num


def sum_lists_eval(a, b):

    first_num, second_num = "", ""
    while a:
        first_num += str(a.val)
        a = a.next_
    while b:
        second_num += str(b.val)
        b = b.next_

    return int(first_num) + int(second_num)
