def triangle():
  stars = 1
  for line in range(6):
    print(' ' * (6 - line - 1), end = '')
    print('*' * stars)
    stars += 2


triangle()
triangle()
