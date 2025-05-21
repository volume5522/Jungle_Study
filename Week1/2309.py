heights = [int(input()) for _ in range(9)]
total = sum(heights)

target = total - 100

found = False
for i in range(9):
    for j in range(i + 1, 9):
        if heights[i] + heights[j] == target:
            fake1, fake2 = heights[i], heights[j]
            heights.remove(fake1)
            heights.remove(fake2)
            found = True
            break
    if found:
        break

heights.sort()
for h in heights:
    print(h)
