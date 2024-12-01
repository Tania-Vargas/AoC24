import sys
from collections import Counter

def read_file(file):
  l1 = []
  l2 = []
  with open(file, 'r') as f:
    lines = f.readlines()
  for line in lines:
    elements = line.strip().split()
    l1.append(int(elements[0]))
    l2.append(int(elements[1]))
  return [l1, l2]


if len(sys.argv) != 2:
  sys.exit(f"Uso: python3 {sys.argv[0]} puzzle.txt")

[list1, list2] = read_file(sys.argv[1])
list1_s = sorted(list1)
list2_s = sorted(list2)

diferences = []
for i in range(0, len(list1_s)):
  diferences.append(abs(list1_s[i] - list2_s[i]))

sum = 0
for elem in diferences:
  sum += elem
print(f"Parte 1 {sum}")

# Parte 2
similarity = 0
counts = Counter(list2_s)
for k in list1_s:
  similarity += k * counts[k]

print(f"Parte 2 {similarity}")