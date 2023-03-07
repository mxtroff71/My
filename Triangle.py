def triangle():
  stars = 1
  for line in range(5):
    print(' ' * (5 - line - 1), end = '')
    print('*' * stars)
    stars += 2


<<<<<<< HEAD
triangle()