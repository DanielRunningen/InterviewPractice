# This solution was developed in November of 2020
# All tests passed after 58 minutes and 17 seconds of development time

# Singly-linked lists are already pre-defined in CodeSignal with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def mergeTwoLinkedLists(l1, l2):
    l3 = None
    l3h = None
    while l1 and l2:
        if l1.value < l2.value:
            s = l1
            l1 = l1.next
        else:
            s = l2
            l2 = l2.next
        s.next = None
        if l3:
            l3.next = s
            l3 = l3.next
        else:
            l3h = s
            l3 = s
    if l3:
        if l1 is not None:
            l3.next = l1
        elif l2 is not None:
            l3.next = l2
    else:
        if l1 is not None:
            l3h = l1
        elif l2 is not None:
            l3h = l2
    return l3h
