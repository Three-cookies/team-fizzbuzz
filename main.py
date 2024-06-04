def fizzbuzz(num):
  for i in range(1, num):
    if i % 3 == 0:
      print('fizz')
    elif i % 5 == 0:
      print('buzz')
    elif i % 15 == 0:
      print('fizzbuzz')

n=int(input())
print(fizzbuzz(n))
