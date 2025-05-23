def Enough (height, trees, M):
    return sum((tree - height) for tree in trees if tree > height) >= M

def Trees_Binary_Search(trees, M):
    low, high = 0, max(trees)
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if Enough(mid, trees, M):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

N, M = map(int, input().split())
trees = list(map(int, input().split()))

print(Trees_Binary_Search(trees, M))