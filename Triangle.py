def triangle():
  stars = 1
  for lines in range(6):
    print(' ' * (6 - lines - 1), end = '')
    print('*' * stars)
    stars += 2


triangle()
triangle()
triangle()
