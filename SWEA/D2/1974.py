# Author: Sanghyeon Lee
# Date: April 26, 2024
# Description: Practice for SWEA D2

correct_line = [i for i in range(1, 10)]  # 스도쿠 숫자 체크용 변수

T = int(input())
for test_case in range(1, T + 1):
    board = [list(map(int, input().split())) for _ in range(9)]

    success = True

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # 범위를 벗어나면 break
            if j + 3 > 9:
                break

            # 3x3 격자 추출
            small_board = [row[j:j+3] for row in board[i:i+3]]

            # 3x3 격자 요소 추출
            elements = []
            for s_row in small_board:
                elements += s_row

            # 추출한 요소들을 정렬했을 때, 1 ~ 9 까지 다 있는지 확인
            if sorted(elements) != correct_line:
                success = False

            # 3x3 격자의 행에 곂치는 요소가 없는지 확인
            for r in range(i, i+3):
                row = board[r]
                if sorted(row) != correct_line:
                    success = False

            # 3x3 격자의 열에 곂치는 요소가 없는지 확인
            for c in range(j, j+3):
                column = list(zip(*board))[c]
                if sorted(column) != correct_line:
                    success = False

    if not success:
        print(f"#{test_case} 0")
    else:
        print(f"#{test_case} 1")

