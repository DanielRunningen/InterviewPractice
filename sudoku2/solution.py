# This solution was developed in November of 2020
# All tests passed after 1 hour and 3 minutes of development time

import numpy as np

def sudoku2(grid):
   ndgrid = np.array(grid)
   for i in range(9):
      for g in [ndgrid[i], ndgrid[:,i]]:
         unique, counts = np.unique(g, return_counts=True)
         n_counts = dict(zip(unique, counts))
         if '.' in n_counts.keys():
            n_counts.pop('.')
         for k, v in n_counts.items():
            if v > 1:
               return False
   for i in range(3):
      for j in range(3):
         unique, counts = np.unique(ndgrid[i*3:i*3+3,j*3:j*3+3], return_counts=True)
         n_counts = dict(zip(unique, counts))
         if '.' in n_counts.keys():
            n_counts.pop('.')
         for k, v in n_counts.items():
            if v > 1:
               return False
   return True
