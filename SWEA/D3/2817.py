# Author: Sanghyeon Lee
# Date: May 15, 2024
# Description: Practice for SWEA D3


## 조합 풀이법
def combinations(new_arr, c):
    global ans, A
    if sum(new_arr) == K:
        ans += 1
        return
    for i in range(c, len(A)):
        combinations(new_arr + [A[i]], i + 1)

## DFS 풀이법
def dfs(n, sm):
    global ans
    if sm == K:
        ans += 1
        return
    if n == N:
        return
    dfs(n+1, sm + A[n])
    dfs(n+1, sm)


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())

    A = list(map(int, input().split()))

    ans = 0
    # combinations([], 0)
    dfs(0, 0)

    print(f"#{test_case} {ans}")