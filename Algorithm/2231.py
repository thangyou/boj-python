N = int(input())
res = 0
for i in range(1, N + 1):
  nums = list(map(int, str(i)))
  res = sum(nums) + i
  if res == N:
    print(i)
    break
  if i == N:
    print(0)
