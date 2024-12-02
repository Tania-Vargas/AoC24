import sys
if len(sys.argv) != 2:
  sys.exit(f"Uso: python3 {sys.argv[0]} puzzle.txt")

file = sys.argv[1]

# lectura de fichero
informes = []
with open(file, 'r') as f:
  lines = f.readlines()
  levels=[]
  for line in lines:
    levels = [int(num) for num in line.strip().split()]
    informes.append(levels)

# Partes 1
def check_level(inf):
  aumenta = None # 0 aumento 1 diminuye
  for l in range(len(inf)):
    correcto = True
    if l > 0:
      dif = inf[l] - inf[l-1]
      if 0 < abs(dif) <= 3: 
        correcto = True
      else: 
        correcto = False
        break
      if dif < 0: # disminuye
        if aumenta == None: aumenta = 1
        else:
          if aumenta != 1: 
            correcto = False
            break
      elif dif > 0: # aunmenta
        if aumenta == None: aumenta = 0
        else:
          if aumenta != 0: 
            correcto = False
            break
      elif dif == 0: 
        correcto = False
        break
  return correcto

seguro = 0
for inf in informes:
  if check_level(inf): seguro += 1

print(f"Parte 1: {seguro}")

# Parte 2
seguro = 0
for inf in informes:
  aumenta = None # 0 aumento 1 diminuye
  correct = check_level(inf)
  if correct: seguro += 1
  else:
    for l2 in range(len(inf)):
      current = inf.copy()
      current.pop(l2)
      aux_correct = check_level(current)
      if correct != True: correct = aux_correct 
    if correct: seguro += 1

print(f"Parte 2: {seguro}")