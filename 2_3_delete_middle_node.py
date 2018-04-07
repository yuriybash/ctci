class Node(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return 'Node(x=%s)' % self.val


def delete_middle_node(node):

    temp = node.next.val
    while node.next:
        node.val = temp
        if not node.next.next:
            break
        temp = node.next.next.val
        node = node.next
