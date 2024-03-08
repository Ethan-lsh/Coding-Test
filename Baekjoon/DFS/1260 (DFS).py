# Author: Sanghyeon Lee
# Date: March 1, 2024
# Description: Basic of DFS and BFS

def dfs():
    ## DFS
    global N

    while stack:
        current = stack.pop()
        print(current, end=' ')

        if current == N-1:
            break

        if not visited[current]:
            visited[current] = True
            for i in graph[current]:
                if not visited[i]:
                    stack.append(i)


if __name__ == '__main__':
    N, M, V = map(int, input().split())

    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)

    stack = [V]

    dfs()