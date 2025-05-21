N, X = map(int, input().split())
A = list(map(int, input().split()))

def compareArray():
    for num in A:
        if num < X:
            print(num, end=' ')

compareArray()
