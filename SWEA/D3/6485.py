# Author: Sanghyeon Lee
# Date: May 15, 2024
# Description: Practice for SWEA D3

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 버스 노선 수

    cnts = [0] * 5001  # 전체 버스 정류장 개수

    # 주어진 버스 노선에 대해
    for _ in range(N):
        a, b = map(int, input().split())
        # a ~ b 까지의 버스 정류장 번호를 지나면 +1
        for i in range(a, b + 1):
            cnts[i] += 1

    P = int(input())
    ans = []
    # 원하는 버스 정류장 번호에 대해
    for _ in range(P):
        bus_stop = int(input())
        ans.append(cnts[bus_stop])

    print(f"#{test_case}", *ans)
