# Author: Sanghyeon Lee
# Date: April 28, 2024
# Description: Practice for SWEA D2

# 문제에서 주어진 문자표
base64_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

T = int(input())
for test_case in range(1, T + 1):
    encoded_string = list(input())

    decoded_string = ""
    # 24bit 를 6bit씩 잘라 4개의 글자를 만들었기 때문에, 인코딩된 문자열에서 4글자씩 가져온다.
    for i in range(0, len(encoded_string), 4):
        partial_string = encoded_string[i:i+4]

        # 문자표에서 각 글자에 해당하는 값을 찾는다
        idx_partial_string = [base64_table.index(p) for p in partial_string]

        bin_idx = ""
        # 각 글자의 값을 이진 표현으로 변경
        for idx_partial in idx_partial_string:
            bin_idx += (format(idx_partial, "06b"))

        # 이진 표현으로 변경된 값을 아스키코드 테이블을 사용해 디코딩 한다.
        for j in range(0, len(bin_idx), 8):
            decimal_bin_idx = int('0b'+bin_idx[j:j+8], 2)
            decoded_word = chr(decimal_bin_idx)
            decoded_string += decoded_word

    print(f"#{test_case} {decoded_string}")