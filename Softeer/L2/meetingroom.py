# Author: Sanghyeon Lee
# Date: June 17, 2024
# Description: Practice for Softeer, L2

N, M = map(int, input().split())
rooms = {}

for _ in range(N):
    room = input()
    rooms[room] = [0]*18 + [1]


for _ in range(M):
    room_name, s, e = input().split()
    s = int(s)
    e = int(e)
    for i in range(s, e):
        rooms[room_name][i] = 1

rooms = dict(sorted(rooms.items()))

for index, room in enumerate(rooms):
    print(f'Room {room}:')
    times = []
    current = 1
    # 9시 ~ 18시까지
    for i in range(9, 19):
        # 현재 방이 비어있고 회의가 없을 때, 시작 시간을 설정
        if current == 1 and rooms[room][i] == 0:
            start = i
            current = 0
        # 현재 방이 차있고 회의가 있을 때, 종료 시간을 설정
        # [시작, 종료] 시간을 현재 방의 타임테이블에 추가
        elif current == 0 and rooms[room][i] == 1:
            end = i
            current = 1
            times.append([start, end])

    if len(times) == 0:
        print('Not available')
    else:
        print(f'{len(times)} available:')
        for x in times:
            print(f'{x[0]:02d}-{x[1]}')

    if index != len(rooms) - 1:
        print('-----')



