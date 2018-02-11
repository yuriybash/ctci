def palindrome_permutation(s):
    arr = list(s)

    perms = []
    first_char = arr.pop(0)
    if len(arr) == 0:
        return [[first_char]]

    perms_returned = palindrome_permutation(arr)

    for perm in perms_returned:
        perm.insert(0, first_char)
        print "adding", perm
        perms.append(perm)

    return perms


palindrome_permutation("abcdef")  # false
print palindrome_permutation("tact coa")  # true - "taco cat"
