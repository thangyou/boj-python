N = int(input())  # 줄 수
sorted_N = sorted(list([int(input()) for _ in range(N)]))
for i in range(N):
  print(sorted_N[i])
