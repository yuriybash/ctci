def urlify_in_place(s):
    """
    strings are immutable, so we at least do it with O(N) space
    """
    escaped = ""
    for c in s:
        escaped += '%20' if c == ':' else c

    return escaped
