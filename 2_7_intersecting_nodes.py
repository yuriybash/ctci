class Node(object):

    def __init__(self, val, next_=None):
        self.val = val
        self.next_ = next_

    def __repr__(self):
        return 'Node(x=%s)' % self.val


def intersect(head_1, head_2):

    node_1 = head_1
    ll_1_nodes = set()
    while node_1:
        ll_1_nodes.add(node_1)
        node_1 = node_1.next_

    node_2 = head_2
    while node_2:
        if node_2 in ll_1_nodes:
            return True
        node_2 = node_2.next_

    return False
