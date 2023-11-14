N, k = map(int, input().split())
x = sorted(list(map(int, input().split())))  # reverse=False
print(x[N - k])