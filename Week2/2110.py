def possible(distance, houses, C):
    count = 1
    last_install = houses[0]
    for house in houses[1:]:
        if house - last_install >= distance:
            count += 1
            last_install = house
    return count >= C

def house_Binary_Search(houses, C) :
    houses.sort()
    left = 1
    right = (houses[-1] - houses[0])//(C-1)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if possible(mid, houses, C):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result


N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

print(house_Binary_Search(houses, C))