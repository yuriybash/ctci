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
