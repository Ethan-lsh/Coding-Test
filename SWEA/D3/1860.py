# Author: Sanghyeon Lee
# Date: May 15, 2024
# Description: Practice for SWEA D3

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())

    arrival = list(map(int, input().split()))  # 각 사람이 도착하는 초 단위위
    arrival.sort()

    # 모든 손님들이 기다리는 시간 없이 붕어빵을 가져갈 수 있어야 함
    success = True
    for i in range(N):
        # M초에 붕어빵 개수를 고려하지 않고
        # 각 손님이 도착하는 시간에 나올 수 있는 붕어빵의 개수에 다녀간 손님의 수를 뺀다
        taco = (arrival[i] // M) * K - (i + 1)
        if taco < 0:
            success = False
            break

    print(f"#{test_case}", "Possible" if success else "Impossible")