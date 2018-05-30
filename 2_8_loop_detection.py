class Node(object):

    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = next_

    def __repr__(self):
        return 'Node(x=%s)' % self.val


def loop_detection(head):
    seen = set()
    node = head

    # alternatively, could do tortoise/hare
    while node:
        if node in seen:
            return node
        seen.add(node)
        node = node.next_
    return False
