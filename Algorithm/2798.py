# brute force
# 완전 탐색 알고리즘
# 가능한 모든 경우의 수를 탐색하면서 요구 조건에 충족되는 결과만을 가져온다
# 알고리즘 설계의 가장 기본적인 접근법
#   - 해가 존재할 것이라 예상되는 모든 영역을 전체 탐색
#   - 순차탐색, 깊이우선탐색(DFS), 너비우선탐색(BFS)

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
