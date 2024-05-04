# Author: Sanghyeon Lee
# Date: April 8, 2024
# Description: Practice for SWEA D3

def check_palindrome(arr):
    global ans
    for k in range(8):
        # 배열 범위를 넘으면 다음 행 or 열로 이동
        if k + length > 8:
            break

        sentence = arr[k:k + length]
        # 처음과 마지막 문자가 같을 때만, 회문을 체크
        if sentence[0] == sentence[-1]:
            ans += 1 if sentence == sentence[::-1] else 0

for test_case in range(1, 11):
    length = int(input())
    board = [list(input()) for _ in range(8)]

    ans = 0

    # 행 탐색
    for row in board:
        check_palindrome(row)

    # 열 탐색
    for column in list(zip(*board)):
        check_palindrome(column)

    print(f"#{test_case} {ans}")