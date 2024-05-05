# Author: Sanghyeon Lee
# Date: May 5, 2024
# Description: Practice for SWEA D3

# import sys
# sys.stdin = open("../input.txt", "r")

T = 10
for test_case in range(1, T + 1):
    width = int(input())

    # 1 = N극; 2 = S극
    table = [list(map(int, input().split())) for _ in range(width)]

    ans = 0

    # 무조건 N극은 아래로, S극은 위로 이동한다.
    # 따라서, column에서 0을 제거했을 때 '12'의 개수를 찾으면 교착상태의 개수와 같다.
    for col in list(zip(*table)):
        without_zero = [c for c in col if c > 0]
        col_str = "".join(map(str, without_zero))
        ans += col_str.count("12")

    print(f"#{test_case} {ans}")
