# Author: Sanghyeon Lee
# Date: April 27, 2024
# Description: Practice for SWEA

T = int(input())
for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())

    A_company = P * W

    B_company = 0
    if R >= W:   # 사용량이 같거나 작아도 기본 요금
        B_company = Q
    else:
        B_company = Q + abs(R - W) * S

    print(f"#{test_case}", A_company if A_company < B_company else B_company)