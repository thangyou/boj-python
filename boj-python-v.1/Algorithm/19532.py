a, b, c, d, e, fs = map(int, input().split())

for x in range(-999, 1000):
  for y in range(-999, 1000):
    if (a * x) + (b * y) == c and (d * x) + (e * y) == f:
      print(x, y)

# 역행렬 이용
'''
# 수식
ax + by = c
dx + ey = f

# 수식 -> 배열
[[a, b], [d, e]] * [x, y] = [c, f]
A * X = B

# 수식에서 ad-bc 부분
k = a*e-b*d

# x, y 행렬곱 식을 풀어서 넣음
print((e*c-b*f)//k, (-c*d+a*f)//k)
'''