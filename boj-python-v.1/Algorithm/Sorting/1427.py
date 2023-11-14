N = int(input())
arr = list(map(int, str(N)))

arr.sort(reverse=True)  # 내림차순

for i in arr:
  print(i, end='')
