def factorial(n):
  res = 1
  if n > 0:
    res = n * factorial(n - 1)
  return res


N = int(input())
print(factorial(N))
