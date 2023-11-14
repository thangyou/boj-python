nums = map(int, input().split())
res = 0
for n in nums:
  res += n**2
print(res % 10)
