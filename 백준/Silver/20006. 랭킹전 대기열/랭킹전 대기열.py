# 20006. 랭겜 대기열
p, m = map(int, input().split())
players = {}
inp_order = []
player_status = {}
total_rooms = [] # 딕셔너리가 나열될 리스트 생성. 순서는 방 생성 순서와 같음.
for i in range(p):
    l, n = input().split()
    players[n] = int(l)
    player_status[n] = False
    inp_order.append(n)
#입력 완료, 플레이어 닉:레벨 딕셔너리, 닉 입력 순서 리스트.

# 새 방을 만드는 조건 : 신규 유저가 모든 방의 레벨 기준보다 낮을 때, 또는 모든 방의 인원이 다 찼을 때
# 모든 방의 인원이 다 찼는지부터 확인하고, 그렇지 않다면 신규 유저가 빈 방의 요구레벨을 충족하는지 확인

# 일단 첫 유저의 새 방 만들기
def making_room(n, l) :
    global m
    room = {}
    room['num_'] = 1 # 방 인원수를 딕셔너리 항목에 추가'
    room['status_'] = 'Waiting!' #방 상태 항목 추가
    room[n] = int(l)
    room['lv_'] = int(l)
    if m == 1 :
        room['status_'] = 'Started!'
    return room #{'num' : 1, n : l}

total_rooms.append(making_room(inp_order[0], players[inp_order[0]]))

for ply in inp_order[1::] : # 각 플레이어(첫번째 플레이어는 방을 만들었으므로 두번째부터)
    for room in total_rooms : #플레이어별 맞는 방 탐색
        if room['num_'] < m and player_status[ply] == False : #방 인원수 충족하고
            if room['lv_']-10 <= players[ply] <= room['lv_']+10 :#기준 레벨 범위(방장 +=- 10) 안이면
                room[ply] = int(players[ply]) # 닉 : 레벨 딕셔너리에 추가
                room['num_'] += 1 # 방 인원 추가
                player_status[ply] = True
                if room['num_'] == m : # 풀방되면
                    room['status_'] = 'Started!'
                    break
            else : # 레벨 기준 충족 못하면
                # total_rooms.append(making_room(ply, players[ply])) # 얘 이름으로 방 생성
                continue # 다음방으로
        else : # 인원수 맞지 않으면
            continue # 다음방으로
    #플레이어의 전체 방 탐색 종료
    if player_status[ply] == False :
        total_rooms.append(making_room(ply, players[ply])) # 얘 이름으로 방 생성
            
for room in total_rooms :
    print(room['status_'])
    room.pop('status_') # 방 상태 키 제거
    room.pop('num_') # 인원수 키 제거
    room.pop('lv_') # 기준 레벨 제거
    room_sorted = sorted(room) # 알파벳순 출력순서 정렬
    for p in room_sorted :
        print(room[p], p)