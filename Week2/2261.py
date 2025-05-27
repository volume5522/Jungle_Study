import sys
import bisect

input = sys.stdin.readline

n = int(input())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort()

def dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2

def brute_force(start, end):
    min_dist = float('inf')
    for i in range(start, end):
        for j in range(i + 1, end):
            min_dist = min(min_dist, dist(points[i], points[j]))
    return min_dist

def find_min_dist(start, end):
    size = end - start
    if size < 3:
        return brute_force(start, end)

    mid = (start + end) // 2
    left = find_min_dist(start, mid)
    right = find_min_dist(mid, end)
    min_dist = min(left, right)

    mid_x = points[mid][0]
    lower = mid_x - int(min_dist**0.5)
    upper = mid_x + int(min_dist**0.5)

    left_idx = bisect.bisect_left(points, (lower, -float('inf')), lo=start, hi=end)
    right_idx = bisect.bisect_right(points, (upper, float('inf')), lo=start, hi=end)
    band_points = points[left_idx:right_idx]
    band_points.sort(key=lambda x: x[1])

    for i in range(len(band_points)):
        for j in range(i + 1, min(i + 7, len(band_points))):
            if (band_points[j][1] - band_points[i][1])**2 >= min_dist:
                break
            d = dist(band_points[i], band_points[j])
            min_dist = min(min_dist, d)
    return min_dist

print(find_min_dist(0, n))
