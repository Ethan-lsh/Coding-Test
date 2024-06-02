# Author: Sanghyeon Lee
# Date: June 1, 2024
# Description: Practice for SWEA D4

order = {'<': (0, -1),
         '>': (0, 1),
         '^': (-1, 0),
         'v': (1, 0)}

def nextStep(characters, visited, dir, num, pos):
    while pos:
        letter = characters[pos[0]][pos[1]]

        if letter == '@':
            return True

        if (dir, num) in visited[pos[0]][pos[1]]:
            return False
        visited[pos[0]][pos[1]].append((dir, num))

        if letter == "?":
            all = ["<", ">", "v", "^"]
            while all:
                nextdir = all.pop()
                if nextStep(characters, visited, nextdir, num, nextPos(nextdir, pos)):
                    return True
        else:
            if letter.isdigit():
                num = int(letter)

            if letter in order.keys():
                dir = letter

            if letter == "_":
                dir = ">" if num == 0 else "<"

            if letter == "|":
                dir = "v" if num == 0 else "^"

            if letter == "+":
                if num == 15:
                    num = 0
                else:
                    num += 1

            if letter == "-":
                if num == 0:
                    num = 15
                else:
                    num -= 1

            pos = nextPos(dir, pos)

def nextPos(dir, current_pos):
    r, c = current_pos

    tr, tc = order[dir]
    temp_r, temp_c = r + tr, c + tc

    if temp_r < 0 or temp_c < 0 or temp_r >= R or temp_c >= C:
        if dir == "<":
            temp_c = C - 1
        elif dir == ">":
            temp_c = 0
        elif dir == "^":
            temp_r = R - 1
        elif dir == "v":
            temp_r = 0
    return (temp_r, temp_c)


def solve(characters, visited):
    end = 0
    end_point = []
    for qi in range(R):
        for qv in range(C):
            if characters[qi][qv] == '@':
                end += 1
                end_point.append((qi, qv))
    if end < 1:
        return "NO"

    for pos in end_point:
        r, c = pos
        bad_count = 0

        for dx, dy in order.values():
            temp_r, temp_c = r + dx, c + dy
            if 0 <= temp_r < R and 0 <= temp_c < C:
                if characters[temp_r][temp_c] in order.keys():
                    bad_count += 1
                else:
                    bad_count = 0
                    break

        if bad_count == 4:
            end -= 1

    if end < 1:
        return "NO"

    if nextStep(characters, visited, '>', 0, (0, 0)):
        return "YES"
    else:
        return "NO"


T = int(input())
for test_case in range(1, T + 1):
    R, C = map(int, input().split())
    characters = [list(input()) for _ in range(R)]

    visited = []
    for vi in range(R):
        visit = []
        for ic in range(C):
            visit.append([])
        visited.append(visit)

    print(f"#{test_case} {solve(characters, visited)}")
