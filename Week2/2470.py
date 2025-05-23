def binary_search(arr):
    arr.sort()
    N = len(arr)
    min_sum = float('inf')
    result = (0, 0)

    for i in range(N - 1):
        left = i + 1
        right = N - 1
        while left <= right:
            mid = (left + right) // 2
            total = arr[i] + arr[mid]
            if abs(total) < min_sum:
                min_sum = abs(total)
                result = (arr[i], arr[mid])
            if total < 0:
                left = mid + 1
            else:
                right = mid - 1

    return result

N = int(input())
arr = list(map(int, input().split()))
a, b = binary_search(arr)
print(a, b)