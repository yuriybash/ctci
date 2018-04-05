class Node(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return 'Node(x=%s)' % self.val


def kth_to_last(head, k):

    count = 0
    node = head
    while node:
        count += 1
        node = node.next

    node = head
    target = count - k
    count = 0
    while node:
        if count == target:
            return node
        count += 1
        node = node.next
