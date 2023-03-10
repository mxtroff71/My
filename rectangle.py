def rectangle():
  for line in range(5):
    if line == 0 or line == 4:
      print('*')
    else:
      print('*' + ' ' * 3 + '*')
rectangle()
rectangle()