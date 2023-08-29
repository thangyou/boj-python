# 시간복잡도 O(nlogn) 인 정렬 = merge sort
# 시간 초과
'''
N = int(input())
sorted_N = sorted(set([int(input()) for _ in range(N)]))
for i in sorted_N[i]:
  print(i)
'''
import sys

input = sys.stdin.readline
N = int(input())
# sorted_N = []

sorted_N = sorted(list([int(input()) for _ in range(N)]))

# for i in range(N):
#   sorted_N.append(int(input()))

# for i in sorted(sorted_N):
for i in sorted_N:
  print(i)
