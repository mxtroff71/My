def rectangle():
  for line in range(6):
    if line == 0 or line == 5:
      print('*')
    else:
      print('*' + ' ' * 3 + '*')
rectangle()
rectangle()