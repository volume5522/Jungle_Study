import sys
input = sys.stdin.readline

white = 0 #초기화 
blue = 0

def count_color(x, y, size, paper):
    global blue, white
    first_color = paper[x][y] # 정사각형 처음 인덱스 색
    same = True # 같으면 1

    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != first_color: # 하나라도 색 다르면 0 
                same = False
                break
        if not same: # 같으면 1
            break

    if same:
        if first_color == 0: # 처음색이 흰색이면 white count 1
            white += 1
        else: # 아니면 blue count 1
            blue += 1
    else: # 색다르면 분할해서 재귀 돌리기 
        half = size // 2
        count_color(x, y, half, paper) 
        count_color(x, y + half, half, paper)
        count_color(x + half, y, half, paper)
        count_color(x + half, y + half, half, paper)

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

count_color(0, 0, N, paper) # 0,0이 현재위치

print(white)
print(blue)
