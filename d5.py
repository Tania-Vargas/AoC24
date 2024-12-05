import sys
import numpy as np
import re

if len(sys.argv) != 2:
  sys.exit(f"Uso: python3 {sys.argv[0]} puzzle.txt")
file = sys.argv[1]

# Lectura de fichero
rules = []
updates = []
with open(file, 'r') as f:
  for l in f:
    if re.search(r'(\d+)\|(\d+)', l) != None:
      rules.append(l.strip().split('|'))
    elif len(l) > 1:
      updates.append(l.strip().split(','))

# Parte 1
def check_update(update):
  for e1 in range(len(update)):
    for e2 in range(len(update)):
      if e1 < e2:
        if [update[e2], update[e1]] in rules:
          return False
  return True

# Parte 2
def ordered_update(update):
  ordered = update
  unorder = True
  while unorder: 
    unorder = False
    for e1 in range(len(ordered)):
      for e2 in range(len(ordered)):
        if e1 < e2:
          if [ordered[e2], ordered[e1]] in rules:
            unorder = True
            aux = ordered[e1]
            ordered[e1] = ordered[e2]
            ordered[e2] = aux
          if unorder: break
  return ordered

# Común
r1 = 0
correct_updates = []
ignored_updates = []
for u in updates:
  if check_update(u):
    correct_updates.append(u)
  else:
    ignored_updates.append(u)
for c in correct_updates:
  center = len(c)//2
  r1 += int(c[center])

r2 = 0
order_updates = []
for i in ignored_updates:
  order_updates.append(ordered_update(i))
  center = len(i)//2
  r2 += int(i[center])

print(f"Parte 1: {r1}")
print(f"Parte 2: {r2}")