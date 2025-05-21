def solve_n_queens(n):  # n x n 체스판에서 n개의 퀸을 놓는 경우의 수를 구하는 함수
    def dfs(row):  # 현재 row(행)에 퀸을 놓기 위한 재귀 함수
        nonlocal count  # 바깥에 있는 count 변수를 사용하기 위해 nonlocal 선언
        if row == n:  # 모든 행에 퀸을 하나씩 놓았다면 (해결된 경우)
            count += 1  # 가능한 경우의 수를 1 증가시키고
            return      # 함수 종료 (백트래킹 시작)

        for col_index in range(n):  # 0부터 n-1까지 모든 열을 탐색
            # 현재 위치(row, col_index)에 퀸을 놓을 수 있는지 확인
            if not col[col_index] and not diag1[row + col_index] and not diag2[row - col_index + n - 1]:
                # 퀸을 (row, col_index)에 임시로 배치
                col[col_index] = True  # 해당 열에는 퀸이 있음
                diag1[row + col_index] = True  # ↘ 방향 대각선에도 퀸이 있음
                diag2[row - col_index + n - 1] = True  # ↙ 방향 대각선에도 퀸이 있음

                dfs(row + 1)  # 다음 행에 퀸을 놓기 위해 재귀 호출

                # 백트래킹: 위에서 퀸을 놓았던 위치를 다시 비워줌 (되돌리기)
                col[col_index] = False
                diag1[row + col_index] = False
                diag2[row - col_index + n - 1] = False

    count = 0  # 가능한 퀸 배치 방법의 총 개수

    # 각 열에 퀸이 있는지 여부를 저장하는 배열 (세로 충돌 체크용)
    col = [False] * n

    # ↘ 대각선 충돌을 확인하는 배열 (row + col 값이 같은 대각선)
    diag1 = [False] * (2 * n - 1)

    # ↙ 대각선 충돌을 확인하는 배열 (row - col + n - 1 값이 같은 대각선)
    diag2 = [False] * (2 * n - 1)

    dfs(0)  # 첫 번째 행부터 퀸 배치를 시작

    return count  # 가능한 전체 배치 방법의 수를 반환


# 사용자로부터 n 값을 입력받고 결과 출력
n = int(input())
print(solve_n_queens(n))
