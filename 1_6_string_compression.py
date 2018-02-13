def string_compression(s):
    compressed = ""

    curr = None;
    count = 0;
    for c in s:

        if c != curr:
            if count:
                compressed += str(count)
                curr = c;
                compressed += curr;
                count = 1;
            else:
                curr = c;
                compressed += curr;
                count = 1;
        else:
            count += 1
    compressed += str(count)

    return compressed
