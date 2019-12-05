import numpy as np


with open('day3.input') as f:
  text = f.read()

t1, t2 = text.split('\n')
t1 = t1.split(',')
t2 = t2.split(',')

w1 = [(s[0], int(s[1:])) for s in t1]
w2 = [(s[0], int(s[1:])) for s in t2]

mat = np.zeros((10000, 10000, 2))
start = np.array([1500, 1500])


'''
    0, -1
-1, 0    1, 0
    0, 1
'''

def iter_wire(w, arr, start, add):
  cur = start
  for axis, dist in w:
    goal = [i for i in cur]
    if axis == 'R':
      goal[0] += dist
      arr[(cur[0]+1):(goal[0]+1),cur[1], add] += 1
    elif axis == 'L':
      goal[0] -= dist
      arr[goal[0]:cur[0],cur[1], add] += 1
    elif axis == 'U':
      goal[1] -= dist
      arr[cur[0],goal[1]:cur[1], add] += 1
    elif axis == 'D':
      goal[1] += dist
      arr[cur[0],(cur[1]+1):(goal[1]+1), add] += 1
    cur = goal
  return arr


tw1 = [(s[0], int(s[1:])) for s in 'R8,U5,L5,D3'.split(',')]
res = iter_wire(tw1, np.zeros((12, 12,2)), np.array([1, 8]), 1)
# print(res)

p1 = iter_wire(w1, mat, start, 1)
p2 = iter_wire(w2, p1, start, 0)
print(p2)

