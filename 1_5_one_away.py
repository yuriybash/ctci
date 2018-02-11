def one_away(s1, s2):

    diff = abs(len(s1) - len(s2))

    if diff >= 2:
        return False
    elif diff == 0:
        return sum(s1[i] != s2[i] for i in range(len(s1))) <= 1
    else:
        if len(s1) > len(s2):
            temp = s1;
            s1 = s2;
            s2 = temp;

        for idx in range(len(s1)):
            if s1[idx] != s2[idx]:
                return s1[:idx] + s2[idx] + s1[idx:] == s2
        return True
