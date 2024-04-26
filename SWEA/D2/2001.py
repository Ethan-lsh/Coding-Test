# Author: Sanghyeon Lee
# Date: April 26, 2024
# Description: Practice for SWEA D2

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]

    score = 0   # 영역 안의 점수
    
    # 주어진 2차원 배열의 인덱스를 하나씩 증가시킨다
    for i in range(N):
        for j in range(N):
            # 만약, 선택 영역이 범위를 벗어나면 break
            if i + M > N:
                break

            # 2차원 배열 슬라이싱으로 원하는 영역을 추출
            stamp = [row[j:j+M] for row in board[i:i+M]]

            tmp = 0
            for row in stamp:
                tmp += sum(row)
            
            # 현재 영역의 점수가 기존 점수보다 크면 업데이트
            score = max(score, tmp)

    print(f"#{test_case} {score}")