A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)

for digit in range(10):
    print(result.count(str(digit)))
