# Author: Sanghyeon Lee
# Date: March 4, 2024
# Description: Practice for Backtracking

N = int(input())

status = [list(map(int, input().split())) for _ in range(N)]

visited = [False for _ in range(N)]

minimum = 100

def backtracking(num, player):
    '''
    최소값을 찾기 위한 함수
    :param num: 선택된 선수의 총 인원수
    :param player: 선택된 선수의 번호
    :return: 최솟값
    '''
    global minimum
    if num == N//2:  # 만약, 선택된 총 인원수가 팀 구성원 수와 같다면
        s_team = 0
        l_team = 0

        # 모든 테이블을 탐색한다.
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:  # 아래의 for 문에서 선택된 선수라면
                    s_team += status[i][j]   # s team에 추가
                if not visited[i] and not visited[j]:  # 아래의 for 문에서 선택하지 않은 선수라면
                    l_team += status[i][j]  # l team에 추가
        minimum = min(minimum, abs(s_team-l_team))  # 절대값을 취해 차를 무조건 양수로 바꿈
        return


    # 다음 backtracking에서 동일한 선수를 선택하지 않기 위해 range(player, N) 으로 설정
    for i in range(player, N):
        if not visited[i]:  # i가 만약 선택하지 않은 선수라면
            visited[i] = True  # i를 선택
            backtracking(num+1, i+1)  # 총 인원수를 1증가, i+1 이후의 선수로 범위를 줄임
            visited[i] = False # 복귀하면 다시 선택하지 않은 상태로 변경


if __name__ == '__main__':
    backtracking(0, 0)
    print(minimum)
