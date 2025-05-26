import sys
input = sys.stdin.readline

MOD = 1000

def mat_mul(A, B):
    n = len(A)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += A[i][k] * B[k][j]
            result[i][j] %= MOD
    return result

def mat_pow(matrix, exp):
    if exp == 1:
        return [[elem % MOD for elem in row] for row in matrix]
    
    half = mat_pow(matrix, exp // 2)
    temp = mat_mul(half, half)
    
    if exp % 2 == 1:
        return mat_mul(temp, matrix)
    else:
        return temp

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
result = mat_pow(A, B)

for row in result:
    print(*row)
