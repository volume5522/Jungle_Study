import sys
input = sys.stdin.readline

def max_area(hist, start, end):
    if start == end:
        return hist[start]

    mid = (start + end) // 2
    left_area = max_area(hist, start, mid)
    right_area = max_area(hist, mid + 1, end)

    low = mid
    high = mid + 1
    height = min(hist[low], hist[high])
    max_middle_area = height * 2

    while start < low or high < end:
        if high == end or (low > start and hist[low - 1] >= hist[high + 1 if high + 1 <= end else high]):
            low -= 1
            height = min(height, hist[low])
        else:
            high += 1
            height = min(height, hist[high])
        max_middle_area = max(max_middle_area, height * (high - low + 1))

    return max(left_area, right_area, max_middle_area)

while True:
    line = input()
    if line.strip() == '0':
        break
    nums = list(map(int, line.strip().split()))
    n = nums[0]
    hist = nums[1:]
    print(max_area(hist, 0, n - 1))
