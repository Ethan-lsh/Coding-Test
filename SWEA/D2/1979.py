# Author: Sanghyeon Lee
# Date: April 27, 2024
# Description: Practice for SWEA

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    board = [list(input().split()) for _ in range(N)]

    match_string = '1' * K

    # 행 순으로 번호 찾기
    row_cnt = 0
    for row in board:
        str_row = "".join(row).split("0")
        row_cnt += str_row.count(match_string)

    col_cnt = 0
    for col in list(zip(*board)):
        str_col = "".join(col).split("0")
        col_cnt += str_col.count(match_string)

    print(f"#{test_case} {row_cnt + col_cnt}")

