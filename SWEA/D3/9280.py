# Author: Sanghyeon Lee
# Date: May 17, 2024
# Description: Practice for SWEA D3

TC = int(input())
for test_case in range(1, TC + 1):
    n, m = map(int, input().split())

    cost = [int(input()) for _ in range(n)]    # 단위 무게당 요금

    weight = [int(input()) for _ in range(m)]  # 차량의 무게게

    for