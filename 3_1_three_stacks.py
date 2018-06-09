class MultipleStackList(object):
    """
    Use one array to hold an arbitrary number of stacks
    """

    SIZE_PER_STACK = 4
    RESIZE_FACTOR = 2
    NUM_STACKS = None
    CURSORS = {}

    def __repr__(self):
        return str(self.container)

    def __init__(self, n_stacks, size=SIZE_PER_STACK):

        self.NUM_STACKS = n_stacks
        self.container = [None] * (n_stacks * size)
        for x in xrange(n_stacks):
            self.CURSORS[x] = [self.SIZE_PER_STACK * x, self.SIZE_PER_STACK * x]

    def add_to_stack(self, stack_num, val):
        if not self.validate(stack_num):
            self.resize()

        self.container[self.CURSORS[stack_num][1]] = val
        self.CURSORS[stack_num][1] += 1

    def validate(self, stack_num):

        last_elem_of_stack_idx = self.CURSORS[stack_num][1]
        if last_elem_of_stack_idx + 1 > self.CURSORS[stack_num+1][0]:
            return False
        return True

    def resize(self):
        temp = self.container
        self.container = [None] * len(self.container) * self.RESIZE_FACTOR

        for stack_num in xrange(self.NUM_STACKS):
            start_idx = stack_num*self.SIZE_PER_STACK
            for idx in xrange(start_idx, start_idx+self.SIZE_PER_STACK):
                if temp[idx] == None:
                    break
                self.container[start_idx*2+(idx-start_idx)] = temp[idx]

        for k, v in self.CURSORS.iteritems():
            temp = v[1] - v[0]
            v[0]*=self.RESIZE_FACTOR
            v[1] = v[0] + temp
        self.SIZE_PER_STACK *= 2
