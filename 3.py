def name(a, b, c):
  print('{}.{}.{}.'.format(a[0], b[0], c[0]))
inp_name = input('Введите имя, фамилию, отчество через пробел: ').split() # example: Михаил Иванович Кузнецов
name(*inp_name)
