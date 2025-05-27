import bisect
from sys import stdin
input = stdin.readline

M, N, L = map(int, input().split())
hunters = list(map(int, input().split()))
hunters.sort()

count = 0

for _ in range(N):
    x, y = map(int, input().split())
    if y > L:
        continue
    Minpossiblehunt = x - (L - y)
    Maxpossiblehunt = x + (L - y)
    idx = bisect.bisect_left(hunters, Minpossiblehunt)
    if idx < M and hunters[idx] <= Maxpossiblehunt:
        count += 1

print(count)
