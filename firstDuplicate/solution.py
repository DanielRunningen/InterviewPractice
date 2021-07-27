# This solution was developed in November of 2020
# All tests passed after 11 minutes of development time

def firstDuplicate(a):
    b = set()
    for x in a:
        if x in b:
            return x
        b.add(x)
    return -1
