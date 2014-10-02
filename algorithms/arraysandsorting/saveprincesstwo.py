#!/usr/bin/python
def nextMove(n,r,c,grid):
  p  = ()

  for i in range(n):
    for j in range(n):
      if "p" == grid[i][j]:
        p = i,j
  
  if(p[0] > r):
    return "DOWN"
  if(p[0] < r):
    return "UP"
  if(p[1] < c):
    return "LEFT"
  if(p[1] > c):
    return "RIGHT"

'''n = input()
r,c = [int(i) for i in raw_input().strip().split()]
grid = []
for i in xrange(0, n):
    grid.append(raw_input())

print nextMove(n,r,c,grid)'''
