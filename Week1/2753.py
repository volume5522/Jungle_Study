#https://www.acmicpc.net/problem/2753
user_input_year=int(input(""))

if (user_input_year % 4 == 0 and user_input_year % 100 != 0) or (user_input_year % 400 == 0):
    print("1")
else : print("0")