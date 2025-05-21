def z(n, x, y, r, c):
    if n == 0:
        return 0
    
    half = 2 ** (n - 1)

    if r < x + half and c < y + half:
        # 0사분면 (왼쪽 위)
        return 0 * half * half + z(n - 1, x, y, r, c)
    elif r < x + half and c >= y + half:
        # 1사분면 (오른쪽 위)
        return 1 * half * half + z(n - 1, x, y + half, r, c)
    elif r >= x + half and c < y + half:
        # 2사분면 (왼쪽 아래)
        return 2 * half * half + z(n - 1, x + half, y, r, c)
    else:
        # 3사분면 (오른쪽 아래)
        return 3 * half * half + z(n - 1, x + half, y + half, r, c)

# 입력 받기
n, r, c = map(int, input("").split())
print(z(n, 0, 0, r, c))
