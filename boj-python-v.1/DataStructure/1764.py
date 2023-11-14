import sys

input = sys.stdin.readline

N, M = map(int, input().split())
S_hear = set()
S_see = set()

for _ in range(N):
  name = input().strip()
  S_hear.add(name)

for _ in range(M):
  name = input().strip()
  S_see.add(name)

result = sorted(list(S_hear & S_see))

print(len(result), *result, sep="\n")
