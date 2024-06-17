# Author: Sanghyeon Lee
# Date: June 17, 2024
# Description: Practice for Softeer, L2

N, M, K = map(int, input().split())

password = "".join(input().split())

user_input = "".join(input().split())

print("secret" if password in user_input else "normal")