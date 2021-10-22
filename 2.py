def func(s):
  s1 = [[s[0][0], s[1][0], s[2][0]], [s[0][1], s[1][1], s[2][1]], [s[0][2], s[1][2], s[2][2]]]
  if sum(s1[0]) == sum(s1[1]) == sum(s1[2]) == sum(s[0]) == sum(s[1]) == sum(s[2]):
    return True
if func([[4, 9, 2], [3, 5, 7], [8, 1, 6]]): # example
  print('Является')
else:
  print('Не является')
