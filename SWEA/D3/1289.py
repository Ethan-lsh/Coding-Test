# Author: Sanghyeon Lee
# Date: May 9, 2024
# Description: Practice for SWEA D3

T = int(input())
for test_case in range(1, T + 1):
    data = list(input())

    init_data = ["0"] * len(data)

    first_one = data.index("1")  # 처음 1이 나온 지점

    ans = 1  # 1이 나온 지점이 있기 때문에 변경 횟수를 1부터 시작

    # 1이 나온 index 뒤부터, 원본 값을 순회
    # 이전 idx가 가리키는 값과 다르면, 변경이 필요하기 때문에 ans += 1
    for idx in range(first_one+1, len(data)):
        if data[idx - 1] != data[idx]:
            ans += 1

    print(f"#{test_case} {ans}")