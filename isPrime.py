def isPrime(number):
  k = 0
  for i in range(2, number // 2 + 1):
    if number % i == 0:
        k += 1
        break
  if k == 0:
    print("Число простое")
  else:
    print("Число составное")
n = int(input('Введите количество чисел в последовательности: '))
for num in range(n):
  number = int(input('Введите число: '))
  isPrime(number)