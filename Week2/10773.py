stack = []

K = int(input())

for _ in range(K) :
    N = int(input())
    if N == 0 :
        stack.pop()
    else :
        stack.append(N)

print(sum(stack))