class Node(object):

    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = next_

    def __repr__(self):
        return 'Node(x=%s)' % self.val


def remove_dupes(node):

    count = {}
    curr_node = node
    while curr_node:
        if curr_node.val in count:
            count[curr_node.val] += 1
        else:
            count[curr_node.val] = 1
        curr_node = curr_node.next_

    curr_node = node
    while curr_node:
        if count[curr_node.next_.val] > 1:
            count[curr_node.next_.val] -= 1
            curr_node.next_ = curr_node.next_.next_
        curr_node = curr_node.next_


def remove_dupes_no_addtl_mem(node):

    first_ptr = node
    while first_ptr:
        second_ptr = first_ptr
        while second_ptr:
            if second_ptr.next_ and second_ptr.next_.val == first_ptr.val:
                second_ptr.next_ = second_ptr.next_.next_
            second_ptr = second_ptr.next_
        first_ptr = first_ptr.next_
