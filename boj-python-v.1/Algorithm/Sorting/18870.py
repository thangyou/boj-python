# list.index(i) : O(n) => 시간 초과
# {dict[요소] : 요소의 index} : O(1)

import sys

input = sys.stdin.readline

N = int(input())
# 5
arr1 = list(map(int, input().split()))
# 2 4 -10 4 -9
arr2 = sorted(set(arr1))
print(arr2)
# [-10, -9, 2, 4]

dic = {arr2[i]: i for i in range(len(arr2))}
# 0~3을 arr의 요소에 넣어줌
# arr[0] = -1, arr[1] = -9, arr[2] = 2, arr[3] = 4

for i in arr1:
  print(dic[i], end=' ')
