def is_valid_walk(walk):
    n = 0
    s = 0
    w = 0
    e = 0

    if len(walk) == 10:
        for letter in walk:
            if letter == "n":
                n += 1
            elif letter == "s":
                s += 1
            elif letter == "w":
                w += 1
            elif letter == "e":
                e += 1
        if n == s and w == e:
            return True
        return False
    else:
        return False
