import sys
import numpy as np

if len(sys.argv) != 2:
  sys.exit(f"Uso: python3 {sys.argv[0]} puzzle.txt")
file = sys.argv[1]

# Lectura de fichero
puzzle = []
with open(file, 'r') as f:
  for l in f:
    puzzle.append(list(l.strip()))

wordh = list("XMAS")
wordhb = list(reversed(wordh))
count = 0

#horizontal 
for i in range(len(puzzle)):
  for j in range(len(puzzle[i])-4+1):
    current=puzzle[i][j:j+4]
    if current == wordh: count+=1
    if current == wordhb: count+=1

#vertical 
for i in range(len(puzzle)-4+1):
  for j in range(len(puzzle[i])):
    current= [puzzle[k][j] for k in range(i, i+4)]
    if current == wordh: count+=1
    if current == wordhb: count+=1

#diagonal principal
for i in range(len(puzzle)-4+1):
  for j in range(len(puzzle[i])-4+1):
    current=[puzzle[i+k][j+k] for k in range(4)]
    if current == wordh: count+=1
    if current == wordhb: count+=1

#diagonal secundaria
for i in range(len(puzzle)-4+1):
  for j in range(3, len(puzzle[i])):
    current=[puzzle[i+k][j-k] for k in range(4)]
    if current == wordh: count+=1
    if current == wordhb: count+=1
print(f"Parte 1: {count}")

# Parte 2
wordx = list("MAS")
wordxb = list(reversed(wordx))
count2 = 0

for i in range(0, len(puzzle)-3+1):
  for j in range(0, len(puzzle[i])-3+1):
    n_puzzle = [row[j:j+3] for row in puzzle[i:i+3]]

    findedP = False
    findedS = False 
    #diagonal principal
    current=[n_puzzle[k][k] for k in range(3)]
    if current == wordx or current == wordxb: findedP = True

    #diagonal secundaria
    current=[n_puzzle[k][2-k] for k in range(3)]
    if current == wordx or current == wordxb: findedS = True

    if findedP and findedS: count2+=1
print(f"Parte 2: {count2}")