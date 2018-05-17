class Node(object):

    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = next_

    def __repr__(self):
        return 'Node(x=%s)' % self.val


def partition(head, x):

    values = []
    node = head
    while node:
        values.append(node.val)
        node = node.next_

    values.sort()
    new_head = new_node = Node(values.pop(0))
    for val in values:
        print "val: ", val
        new_node.next_ = Node(val)
        new_node = new_node.next_

    return new_head
