# This solution was developed in November of 2020
# All tests passed after 30 minutes and 43 seconds of development time

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from helpers.listNode import ListNode

# Singly-linked lists are already pre-defined in CodeSignal with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None

def addTwoHugeNumbers(a, b):
   al = []
   bl = []

   while a:
      al.append(a.value)
      a = a.next
   while b:
      bl.append(b.value)
      b = b.next

   al.reverse()
   bl.reverse()
   aln = len(al)
   bln = len(bl)

   if aln > bln:
      tail, al = al[bln:], al[:bln]
   elif bln > aln:
      tail, bl = bl[aln:], bl[:aln]
   else:
      tail = []

   c = []
   carry = False
   for i in range(len(al)):
      total = al[i] + bl[i]
      if carry:
         total += 1
         carry = False
      if total > 9999:
         carry = True
         total -= 10000
      c.append(total)

   for t in tail:
      if carry:
         t += 1
         carry = False
      if t > 9999:
         carry = True
         t -= 10000
      c.append(t)

   if carry:
      c.append(1)

   last = None
   for x in c:
      current = ListNode(x)
      current.next, last = last, current

   return last
