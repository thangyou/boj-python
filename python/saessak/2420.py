N, M = map(int, input().split())
res = N - M
if res < 0:
  res *= -1
print(res)