def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, limit + 1, i):
                is_prime[j] = False
    return is_prime

def goldbach_partition(n, is_prime):
    for i in range(n // 2, 1, -1):
        if is_prime[i] and is_prime[n - i]:
            return (i, n - i)

T = int(input())
is_prime = sieve(10000)

for _ in range(T):
    n = int(input())
    p1, p2 = goldbach_partition(n, is_prime)
    print(p1, p2)
