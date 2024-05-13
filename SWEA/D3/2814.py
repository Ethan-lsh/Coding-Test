# Author: Sanghyeon Lee
# Date: May 13, 2024
# Description: Practice for SWEA

def dfs(s, v):
    global ans
    ans = max(ans, len(v))

    for n in graph[s]:
        if n not in v:
            dfs(n, v+[n])


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    if N == 1:
        print(f"#{test_case} 1")
        continue

    graph = [[]*(N+1) for _ in range(N+1)]

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    ans = 0
    for s in range(1, N + 1):
        dfs(s, [s])

    print(f"#{test_case} {ans}")
