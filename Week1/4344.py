C = int(input())

for _ in range(C):
    data = list(map(int, input().split()))
    N = data[0]
    scores = data[1:]

    avg = sum(scores) / N
    over = [s for s in scores if s > avg]
    ratio = len(over) / N * 100

    print(f"{ratio:.3f}%")
