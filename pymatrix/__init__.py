from pymatrix.Matrix import *

def inputMat(nrows: int, ncolumns: int):
  m = []
  print("[")
  for r in range(nrows):
    for _ in range(ncolumns):
      v = float(input())
    m[r] = v
  return m
