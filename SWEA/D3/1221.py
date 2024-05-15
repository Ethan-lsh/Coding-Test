# Author: Sanghyeon Lee
# Date: May 15, 2024
# Description: Practice for SWEA D3

my_dict = {"ZRO": 0,
           "ONE": 1,
           "TWO": 2,
           "THR": 3,
           "FOR": 4,
           "FIV": 5,
           "SIX": 6,
           "SVN": 7,
           "EGT": 8,
           "NIN": 9}

# 정렬을 위한 함수
def my_sorting(num: str):
    return my_dict[num]


T = int(input())
for _ in range(1, T + 1):
    test_case, N = input().split()
    N = int(N)

    arr = list(input().split())

    # sorted method를 사용한 정렬 (.sort 를 사용해도 된다)
    sorted_arr = sorted(arr, key=my_sorting)

    print(f"{test_case} {sorted_arr}")