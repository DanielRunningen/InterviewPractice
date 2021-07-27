# This solution was developed in November of 2020
# I left this problem open for longer than I was likely working on it
#   and don't have an accurate time estimate
# It also took me a moment to realize that numpy probably
#   had a function to do this and that I didn't need to
#   re-invent the wheel

from numpy import rot90

def rotateImage(a):
   return rot90(a, 3).tolist()
