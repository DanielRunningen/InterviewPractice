def firstNotRepeatingCharacter(s):
    my_dict = dict()
    for c in s:
        if c in my_dict.keys():
            my_dict[c] += 1
        else:
            my_dict[c] = 1
    dupes = [c for c, n in my_dict.items() if n > 1]
    for c in s:
        if c not in dupes:
            return c
    return '_'
