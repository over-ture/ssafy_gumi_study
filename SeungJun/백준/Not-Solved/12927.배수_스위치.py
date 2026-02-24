# 12927. 배수 스위치

lightbulb_list = list(input()) # 전체 전구 리스트 입력
off_bulbs = [] # 꺼진 전구가 몇 번인지의 리스트

for i in range(len(lightbulb_list)) : # 꺼져 있는 전구의 위치 탐색
    if lightbulb_list[i] == 'N' :
        off_bulbs.append(i + 1)
        

print(off_bulbs)

