class Node(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

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
        curr_node = curr_node.next

    curr_node = node
    while curr_node:
        if count[curr_node.next.val] > 1:
            count[curr_node.next.val] -= 1
            curr_node.next = curr_node.next.next
        curr_node = curr_node.next


def remove_dupes_no_addtl_mem(node):

    first_ptr = node
    while first_ptr:

        # curr_val = first_ptr.val

        second_ptr = first_ptr
        while second_ptr:
            if second_ptr.next and second_ptr.next.val == first_ptr.val:
                second_ptr.next = second_ptr.next.next
            second_ptr = second_ptr.next

        first_ptr = first_ptr.next
