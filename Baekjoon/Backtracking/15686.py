# Author: Sanghyeon Lee
# Date: March 8, 2024
# Description: Practice for Backtracking and Simulation example of SWEA

N, M = map(int, input().split())


def backtracking(cnt, idx):
    global result
    val = 0
    if cnt == M:
        for h in house:
            distance = 2*N  # 집을 바꿀떄마다 거리를 초기화
            for c in choosed:  # 선택된 치킨집들에 대한 치킨 거리를 계산
                tmp = abs(h[0]-c[0]) + abs(h[1] - c[1])
                if tmp < distance:
                    distance = tmp
            # 도시 치킨 거리에 치킨거리 최소값 더하기
            val += distance

        if val < result:
            result = min(result, val)
            return

    # 선택한 치킨집을 제외하고 남은 범위에서 탐색
    for i in range(idx, len(chickens)):
        choosed.append(chickens[i])
        backtracking(cnt+1, i+1)
        choosed.pop()


if __name__ == '__main__':
    # 도시 정보
    city = [list(map(int, input().split())) for _ in range(N)]
    house = []
    chickens = []

    for x in range(N):
        for y in range(N):
            if city[x][y] == 1:
                house.append([x, y])
            if city[x][y] == 2:
                chickens.append([x, y])

    # 선택된 치킨집 정보
    choosed = []

    result = 2 * N * len(house)  # 임의의 결과값을 크게 설정하는 편이 좋음

    for k in range(len(chickens)):
        backtracking(0, k)

    # print(city)
    print(result)