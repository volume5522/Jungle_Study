w, h = map(int, input().split())
n = int(input())

horizontal = [0, h]
vertical = [0, w]

for _ in range(n):
    dir, num = map(int, input().split())
    if dir == 0:
        horizontal.append(num)
    else:
        vertical.append(num)

horizontal.sort()
vertical.sort()

max_h = max(horizontal[i+1] - horizontal[i] for i in range(len(horizontal) - 1))
max_w = max(vertical[i+1] - vertical[i] for i in range(len(vertical) - 1))

print(max_h * max_w)
