# Author: Sanghyeon Lee
# Date: June 16, 2024
# Description: Practice for Softeer, L2

numbers = list(map(int, input().split()))

# 비교군
ascending_numbers = sorted(numbers)
descending_numbers = sorted(numbers, reverse=True)

if numbers == ascending_numbers:
    print("ascending")
elif numbers == descending_numbers:
    print("descending")
else:
    print("mixed")

