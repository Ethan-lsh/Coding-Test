# Author: Sanghyeon Lee
# Date: May 6, 2024
# Description: Practice for SWEA D3


T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())  # 재료의 수, 제한 칼로리

    ingredient = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]  # [점수, 칼로리]

    ans = 0

    dp = [[0]*(L + 1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, L+1):
            if ingredient[i][1] > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-ingredient[i][1]] + ingredient[i][0])

    print(f"{test_case} {dp[N][L]}")