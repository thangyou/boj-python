# stable sort
# 값이 같은 원소의 전후관계가 바뀌지 않는 알고리즘

N = int(input())
member = []

for i in range(N):
  age, name = map(str, input().split())
  member.append([int(age), name])

member.sort(key=lambda x: x[0])
# (age, name)에서 age만 비교

for i in member:
  print(i[0], i[1])
