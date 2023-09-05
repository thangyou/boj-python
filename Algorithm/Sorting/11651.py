import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
  [x, y] = map(int, input().split())
  arr.append([y, x])

arr.sort()

for i in range(N):
  print(arr[i][1], arr[i][0])
