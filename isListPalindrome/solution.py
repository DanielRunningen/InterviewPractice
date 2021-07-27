# Singly-linked lists are already pre-defined in CodeSignal with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def isListPalindrome(l):
   l2 = []
   while l:
      l2.append(l.value)
      l = l.next
   for i in range(len(l2)//2):
      if l2[i] != l2[len(l2)-i-1]:
         return False
   return True
