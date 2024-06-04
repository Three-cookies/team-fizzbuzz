def fizzbuzz(num):
  for i in range(1, num):
    if i % 3 == 0:
      print('fizz')
    elif i % 5 == 0:
      print('buzz')

n=int(input())
print(fizzbuzz(n))
