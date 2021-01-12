def firstDuplicate(a):
    b = set()
    for x in a:
        if x in b:
            return x
        b.add(x)
    return -1
