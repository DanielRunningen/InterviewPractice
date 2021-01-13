from numpy import rot90

def rotateImage(a):
   return rot90(a,3).tolist()
