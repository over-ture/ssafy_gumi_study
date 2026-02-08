p, m = map(int, input().split()) # 플레이어 수 p, 방의 정원 m 입력

players = [] # [[id, level], [id, level]]
rooms = []

for i in range(p):
    l, n = map(str, input().split())
    players.append([n, int(l)]) # player 리스트에 [닉네임, 레벨]로 저장


def create_room(player): # 방 생성
    rooms.append([player[1], player])
    return 

def match_room (player): # 방 정원 체크
    if len(rooms) == 0: # 방이 하나도 없다면
        create_room(player) # 방 생성
        return 
    
    for room in rooms: 
        if len(room) -1 == m: # 방 정원이 찾다면 패스
            continue
        elif player[1] <= room[0] + 10 and player[1] >= room[0] - 10:
            room.append(player)
            return # 레벨이 맞으면 추가
        
    create_room(player) # 방을 찾지 못했다면 방 생성
    return

for player in players: # 매칭 하기
    match_room(player)


for room in rooms: # 출력 시작
    if len(room) -1 == m:
        print('Started!') # 방이 차있으면 Started! 먼저 출력
    else:
        print('Waiting!')
    # 방 맨앞의 레벨 빼고 이름 기준 정렬, 플레이어 정보 출력
    for name, level in sorted(room[1:]): 
        print(level, name)
