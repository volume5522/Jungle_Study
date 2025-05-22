def binary_search(target, arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            right = mid -1
        else:
            left = mid + 1
    return 0

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

m = int(input())
arr2 = list(map(int, input().split()))


for x in arr2:
    if binary_search(x, arr):
        print(1)
    else:
        print(0)