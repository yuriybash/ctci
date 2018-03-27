def is_substring(s1, s2):
    return s1 in s2


def string_rotation(s1, s2):

    return len(s1) == len(s2) and is_substring(s2 in s1+s1)

