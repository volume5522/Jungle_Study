def binary_search(target, arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left

def arr_length(sequence):
    newarr = []
    for num in sequence:
        pos = binary_search(num, newarr)
        if pos == len(newarr):
            newarr.append(num)
        else:
            newarr[pos] = num
    return len(newarr)


N = int(input())
sequence = list(map(int, input().split()))
print(arr_length(sequence))