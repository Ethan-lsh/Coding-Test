# Author: Sanghyeon Lee
# Date: May 17, 2024
# Description: Practice for SWEA D3

T = int(input())
for test_case in range(1, T + 1):
    p, q = map(int, input().split())

    # y = -x + a
    a_p = 0
    a_q = 0
    for i in range(200):
        if p > 0:
            p = p - i  # 그 라인에서 몇번째에 위치한지
            a_p = i    # 몇번째 라인인지
        if q > 0:
            q = q - i
            a_q = i

    p_x = a_p + p     # 라인 번호에 위치를 더하면 x 좌표
    p_y = abs(p) + 1  # y 좌표는 p를 양수로 바꾸고 1을 더하면 나온다.

    q_x = a_q + q
    q_y = abs(q) + 1

    pq_x, pq_y = p_x + q_x, p_y + q_y

    line_ans = pq_x + pq_y
    ans = 0
    for i in range(line_ans-1):
        ans += i
    ans += pq_x

    print(f"#{test_case} {ans}")
