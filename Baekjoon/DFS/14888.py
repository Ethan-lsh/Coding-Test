# Author: Sanghyeon Lee
# Date: March 4, 2024
# Description: Practice for DFS

N = int(input())

operands = list(map(int, input().split()))

# number of operators
# +, -, *, //
op = list(map(int, input().split()))

# ! maximum과 minimum을 반대로 설정
maximum = -1e9
minimum = 1e9

def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(maximum, total)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth+1, total+operands[depth],plus-1, minus, multiply, divide)
    if minus:
        dfs(depth+1, total-operands[depth], plus, minus-1, multiply, divide)
    if multiply:
        dfs(depth+1, total*operands[depth], plus, minus, multiply-1, divide)
    if divide:
        dfs(depth+1, int(total/operands[depth]), plus, minus, multiply, divide-1)


# if __name__ == '__main__':
dfs(1, operands[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)