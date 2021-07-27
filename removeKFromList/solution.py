# Singly-linked lists are pre-defined in CodeSignal with this interface:
# class ListNode(object):
#    def __init__(self, x):
#       self.value = x
#       self.next = None

def removeKFromList(l, k):
   while l is not None and l.value == k:
      l = l.next
   node = l
   while node is not None and node.next is not None:
      if node.next.value == k:
         node.next = node.next.next
      else:
         node = node.next
   return l
