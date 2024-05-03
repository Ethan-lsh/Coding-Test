# Author: Sanghyeon Lee
# Date: May 3, 2024
# Description: Practice for SWEA D3

def dfs(n):
    global answer
    if n == N:
        answer = max(answer, int("".join(map(str, lst))))
        return
    # i <-> j 를 순차적으로 바꿔가며 값을 비교
    for i in range(L-1):
        for j in range(i + 1, L):
            lst[i], lst[j] = lst[j], lst[i]

            chk = int("".join(map(str, lst)))
            # 실행시간을 줄이기 위한 중복 제거 블록
            # 동일한 (실행 횟수, chunk) 값이 없는 경우만 dfs를 실행하여 time complexity를 줄인다
            if (n, chk) not in v:
                dfs(n + 1)
                v.append((n, chk))

            # 바꾼 값을 복원 (필수)
            lst[j], lst[i] = lst[i], lst[j]


T = int(input())
for test_case in range(1, T + 1):
    st, t = map(str, input().split())
    N = int(t)
    lst, v = [], []
    L = len(st)
    answer = 0
    for i in st:
        lst.append(i)
    dfs(0)

    print(f"#{test_case} {answer}")