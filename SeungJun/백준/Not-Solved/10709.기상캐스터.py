H, W = map(int, input().split())

forecast = []
city = [] # 도시 기상
for i in range(H) : # 기상 입력
    city_input = list(input())
    city.append(city_input)

for i in range(H) :
    cnt = 0
    temp = []
    for j in range(W) :
        meet = False
        if city[i][j] == 'c' :
            temp.append(0)
            cnt = 0
            meet = True
        else : 
            cnt += 1
            if meet == True :
                temp.append(cnt)
            else :
                temp.append(-1)

    forecast.append(list(temp))

print(forecast)