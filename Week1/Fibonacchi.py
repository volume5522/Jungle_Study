def Fibonachhi(n):
    if n == 0 : 
        return 0
    if n == 1 : 
        return 1
    else :
        Fibonachhi(n-1)+Fibonachhi(n-2)
