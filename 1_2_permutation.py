from collections import defaultdict


def is_permutation(s1, s2):
    s1_store = defaultdict(lambda: 0)
    for c in s1:
        s1_store[c] += 1
    for c in s2:
        s1_store[c] -= 1
        if s1_store[c] < 0:
            return False
    return True
