def string_compression(s):

    compressed = ""
    curr = None;
    count = 0;
    for c in s:
        if c != curr:
            curr = c;
            if count:
                compressed += str(count)
                compressed += curr;
            else:
                compressed += curr;
            count = 1;
        else:
            count += 1
    compressed += str(count)

    return compressed
