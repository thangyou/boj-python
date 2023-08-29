N, M = map(int, input().split())
li = list(map(int, input().split()))
res = 0

for i in range(N):
  for j in range(i + 1, N):
    for k in range(j + 1, N):
      if li[i] + li[j] + li[k] > M:
        continue
      else:
        res = max(res, li[i] + li[j] + li[k])
print(res)
'''
# 순열 조합 라이브러리 itertools 모듈의 combinations
from itertools import combinations

card_num, target_num = map(int, input().split())
card_list = list(map(int, input().split()))
max_num = 0

for cards in combinations(card_list, 3):
tmp_sum = sum(cards)
if max_num < tmp_sum <= target_num:
  max_num = tmp_sum

print(max_num)
'''
