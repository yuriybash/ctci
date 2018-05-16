class Node(object):

    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = next_

    def __repr__(self):
        return 'Node(x=%s)' % self.val


def delete_middle_node(node):

    temp = node.next_.val
    while node.next_:
        node.val = temp
        if not node.next_.next_:
            break
        temp = node.next_.next_.val
        node = node.next_
