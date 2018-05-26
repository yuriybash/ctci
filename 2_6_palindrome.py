class Node(object):

    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = next_

    def __repr__(self):
        return 'Node(x=%s)' % self.val


def is_palindrome(head):

    node = head
    node_vals = []
    while node:
        node_vals.append(node.val)
        node = node.next_

    return node_vals == node_vals[::-1]
