def hansu(num) :
    count = 0
    for i in range(1, num+1):
        if 1 <= i < 100 :
            count += 1
        if 100 <= i < 1001 and i % 100 // 10 - i // 100 == i % 100 % 10 - i % 100 // 10:
            count += 1
    return count

num = int(input())
print(hansu(num))