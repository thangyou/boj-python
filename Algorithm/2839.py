N = int(input())
cnt = 0
while N >= 0:
  if N % 5 == 0:
    cnt += (N // 5)
    print(cnt)
    break
  N = N - 3  # 5의 배수가 되도록
  cnt += 1
else:
  print(-1)
