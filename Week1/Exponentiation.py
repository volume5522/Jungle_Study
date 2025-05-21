# def exponentiation(b, n):
#     if n==0:
#         return 1
#     else :
#         return n* exponentiation(b,n-1)


def exponentiation(b, n):
    if n == 0:
        return 1
    elif n%2 ==0 :
        half = exponentiation(b, n//2)
        return half * half
    else : 
        return n * exponentiation(b,n-1)
