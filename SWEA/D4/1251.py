def prim(n):
    D[n] = 0
    # G[n][n] = 0 <-- 없어도 된다. 이미 밖에서 자기 자신에게 도달하는 거리는 0 인것으로 초기화 되어있다. ex) G[0][0] = G[1][1] = G[2][2] ... = 0

    U = []
    for _ in range(N):
        mini = float("inf")
        for idx in range(N):
            if  idx in U: continue
            if D[idx] < mini:
                mini = D[idx]
                key = idx
        U.append(key)

        for j in range(N):
            if j in U: continue
            if G[key][j] and G[key][j] < D[j]: #+ D[key] < D[j]:
                D[j] = G[key][j] #+ D[key]


TC = int(input())

for tc in range(1,TC+1):
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())
    # 그래프 생성 / 2차원으로 만들기
    G = [[0] * N for _ in range(N)]

    D = [float("inf")] * N
    for i in range(N):
        for j in range(N):
            G[i][j] = (X[i] - X[j])**2 + (Y[i] - Y[j])**2 # 환경 부담금 구하기
            G[j][i] = G[i][j]

    prim(0)

    ans = 0
    for elem in D:
        ans += elem
    print('#{} {}'.format(tc, round(ans*E)))