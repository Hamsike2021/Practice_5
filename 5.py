s1 = ['а', 'о', 'у', 'ы', 'э', 'я', 'ё', 'ю', 'и', 'е']
def glas(s): # для количества гласных
  k = 0
  for el in s:
    if el in s1:
      k += 1
  return k
def sogl(s): # для количества согласных
  k = 0
  for el in s:
    if el not in s1:
      k += 1
  return k
s = input().lower()
print(glas(s)) # гласные
print(sogl(s)) # согласные
