class Node(object):

    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = next_

    def __repr__(self):
        return 'Node(x=%s)' % self.val


def kth_to_last(head, k):

    count = 0
    node = head
    while node:
        count += 1
        node = node.next_

    node = head
    target = count - k
    count = 0
    while node:
        if count == target:
            return node
        count += 1
        node = node.next_
