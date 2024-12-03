import sys
import re

if len(sys.argv) != 2:
  sys.exit(f"Uso: python3 {sys.argv[0]} puzzle.txt")

file = sys.argv[1]

# Lectura de fichero
lines = ""
with open(file, 'r') as f:
  lines = f.readlines()
# Parte 1
multiplicacion = []
for l in lines:
  multiplicacion += re.findall(r'mul\(\d{1,3},\d{1,3}\)', l)

r1 = 0
for m in multiplicacion:
  d = re.findall(r'\d{1,3}', m)
  r1 += int(d[0]) * int(d[1]) 

print(f"Parte 1: {r1}")

# Parte 2
new_mult = []
for l2 in lines:
  new_mult += re.findall(r'don\'t\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)', l2)

r2 = 0
operate = True
for m2 in new_mult:
  if m2 == 'don\'t()': 
    operate = False
  elif m2 == 'do()':
    operate = True
  else:
    if operate == True:
      d = re.findall(r'\d{1,3}', m2)
      d1 = int(d[0])
      d2 = int(d[1])
      r2 += d1 * d2

print(f"Parte 2: {r2}")