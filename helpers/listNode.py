class ListNode:
   def __init__(self, x):
      self.value = x
      self.next = None

   def toList(self):
      l = [self.value]
      if self.next is not None:
         l.extend(self.next.toList())
      return l

def listToLinkedList(l):
   head = None
   last = None
   while len(l) > 0:
      head = ListNode(l.pop())
      head.next = last
      last = head
   return head
