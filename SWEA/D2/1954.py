# Author: Sanghyeon Lee
# Date: April 24, 2024
# Description: Practice for SWEA

# 우 -> 하 -> 좌 -> 상
# 회전 방향
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # 빈 2차원 리스트를 생성
    board = [[0] * N for _ in range(N)]

    d = 0     # 초기 진행 방향
    x, y = 0, 0
    for num in range(1, N*N+1):
        board[x][y] = num

        nx, ny = x + dx[d], y + dy[d]   # 다음 이동 좌표
        # 다음 좌표가 범위 안에 있고 값이 0일 때
        if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0:
            x, y = nx, ny
        else:
            d = (d + 1) % 4
            x, y = x + dx[d], y + dy[d]

    print(f"#{test_case}")
    for row in board:
        print(*row, end='\n')
