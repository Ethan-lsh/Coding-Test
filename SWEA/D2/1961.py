# Author: Sanghyeon Lee
# Date: April 28, 2024
# Description: Practice for SWEA D2

# 90도 회전 함수
def rotate_90(arr):
    return list(map(list, zip(*arr[::-1])))

# 180도 회전 함수
def rotate_180(arr):
    return [a[::-1] for a in arr[::-1]]

# 270도 회전 함수
def rotate_270(arr):
    return [a[::-1] for a in list(map(list, zip(*arr[::-1])))[::-1]]


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]

    board90 = rotate_90(board)
    board180 = rotate_180(board)
    board270 = rotate_270(board)

    # 출력문
    print(f"#{test_case}")
    for a, b, c in zip(board90, board180, board270):
        print("".join(map(str, a)), "".join(map(str, b)), "".join(map(str, c)))


