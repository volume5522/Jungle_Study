T = int(input())  

for _ in range(T):
    R, S = input().split()
    R = int(R)
    P = ''
    for ch in S:
        P += ch * R
    print(P)
