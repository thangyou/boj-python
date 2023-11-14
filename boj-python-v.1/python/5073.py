# 킹받네 픽스ㅎH줘
while 1:
  a, b, c = map(int, input().split())
  if a == b == c == 0:
    break
  # 가장 긴 변의 길이 > 나머지 두 변의 길이의 합
  max_num = max((a, b, c))
  if max_num > sum((a, b, c)) - max_num:
    print('invalid')
    continue
  elif a == b == c:
    print('Equilateral')
  elif a == b or b == c or c == a:
    print('Isosceles')
  else:
    print('Scalene')
